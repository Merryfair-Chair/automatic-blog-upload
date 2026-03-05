import os
import re
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv
import anthropic

load_dotenv(Path(__file__).parent / ".env")
from wp_publisher import publish_draft
from drive_uploader import upload_blog

PROMPTS_DIR = Path(__file__).parent / "prompts"
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

MODE_MAP = {
    "1": "Standard", "2": "Web Search", "3": "Full Tool Access",
    "standard": "Standard", "web": "Web Search", "full": "Full Tool Access",
}


def pull_latest_prompt():
    result = subprocess.run(["git", "pull"], cwd=Path(__file__).parent, capture_output=True, text=True)
    if result.returncode == 0:
        print("[OK] Pulled latest prompt from GitHub")
    else:
        print("[WARN] Git pull failed -- using local version")


def get_latest_prompt():
    md_files = [f for f in PROMPTS_DIR.glob("*.md") if f.name != "README.md"]
    if not md_files:
        raise FileNotFoundError("No prompt .md files found in prompts/ folder.")
    latest = max(md_files, key=lambda f: f.stat().st_mtime)
    print(f"[OK] Using prompt: {latest.name}")
    return latest.read_text(encoding="utf-8")


def select_mode(text, choice):
    """Keep only the selected MODE block, remove the others."""
    selected = MODE_MAP.get(choice.strip().lower(), "Standard")
    for mode in ["Standard", "Web Search", "Full Tool Access"]:
        if mode == selected:
            continue
        lines = text.split("\n")
        out, inside_block, found_mode = [], False, False
        for i, line in enumerate(lines):
            if line.strip() == "```" and not inside_block:
                # Peek ahead to see if next non-empty line is this mode
                next_lines = [l for l in lines[i+1:i+3] if l.strip()]
                if next_lines and next_lines[0].strip() == f"MODE: {mode}":
                    inside_block = True
                    found_mode = True
                    continue
            if inside_block and line.strip() == "```":
                inside_block = False
                continue
            if not inside_block:
                out.append(line)
        text = "\n".join(out)
    return text


def assemble_prompt(text, inputs):
    text = select_mode(text, inputs["mode"])
    replacements = {
        "[insert topic or seed idea \u2014 vague or specific, either works]": inputs["topic"],
        "[one sentence: who is reading this, what do they care about]": inputs["audience"],
        "[rank on Google / inform / convert / build trust / go viral]": inputs["goal"],
        "[URL to outperform, or leave blank]": inputs.get("competitor_url", ""),
        "[specific keyword to target, or leave blank]": inputs.get("target_keyword", ""),
        "[Top / Middle / Bottom, or leave blank]": inputs.get("funnel_stage", ""),
        "[listicle / guide / comparison / story-led, or leave blank]": inputs.get("format_hint", ""),
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def collect_inputs():
    print("\n" + "=" * 60)
    print("  SEO BLOG PIPELINE")
    print("=" * 60)
    print("\n-- CAPABILITY MODE --")
    print("  1. Standard")
    print("  2. Web Search")
    print("  3. Full Tool Access")
    mode = input("Select mode (1/2/3): ").strip() or "1"
    print("\n-- REQUIRED --")
    topic    = input("TOPIC:    ").strip()
    audience = input("AUDIENCE: ").strip()
    goal     = input("GOAL:     ").strip()
    print("\n-- OPTIONAL (press Enter to skip) --")
    competitor_url = input("Competitor URL:  ").strip()
    target_keyword = input("Target Keyword:  ").strip()
    funnel_stage   = input("Funnel Stage:    ").strip()
    format_hint    = input("Format Hint:     ").strip()
    return {
        "mode": mode, "topic": topic, "audience": audience, "goal": goal,
        "competitor_url": competitor_url, "target_keyword": target_keyword,
        "funnel_stage": funnel_stage, "format_hint": format_hint,
    }


def generate_blog(prompt_text):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    print("\n[...] Generating blog content -- this may take a few minutes...")
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=16000,
        messages=[{"role": "user", "content": prompt_text}]
    )
    return msg.content[0].text


def extract_section(text, n, nxt=None):
    m = re.search(r"\*\*\[" + str(n) + r"\].*?\*\*", text)
    if not m:
        return ""
    start = m.end()
    if nxt:
        m2 = re.search(r"\*\*\[" + str(nxt) + r"\]", text[start:])
        end = start + m2.start() if m2 else len(text)
    else:
        end = len(text)
    return text[start:end].strip()


def parse_response(text):
    title  = extract_section(text, 2, 3).strip("* \n")
    meta   = extract_section(text, 3, 4).strip("* \n")
    slug   = extract_section(text, 4, 5).strip("` \n")
    draft  = extract_section(text, 6, 7)
    faq_s  = extract_section(text, 7, 8)
    fm = re.search(r'(<script type="application/ld\+json">.*?</script>)', faq_s, re.DOTALL)
    return {
        "title": title, "meta_description": meta, "slug": slug,
        "full_draft": draft, "faq_schema": fm.group(1) if fm else "",
        "full_response": text,
    }


def main():
    if not ANTHROPIC_API_KEY:
        print("[ERROR] ANTHROPIC_API_KEY not set in .env file.")
        sys.exit(1)

    pull_latest_prompt()
    inputs = collect_inputs()
    final_prompt = assemble_prompt(get_latest_prompt(), inputs)
    response = generate_blog(final_prompt)
    p = parse_response(response)

    print(f"\n[OK] Blog generated: {p['title']}")
    print(f"     Slug: {p['slug']}")

    drive_link, edit_url = None, ""

    print("\n[...] Saving to Google Drive...")
    try:
        drive_link, fname = upload_blog(p["title"], p["full_draft"], p["faq_schema"])
        print(f"[OK] Saved: {fname}")
        print(f"     {drive_link}")
    except Exception as e:
        print(f"[WARN] Drive upload failed: {e}")

    print("\n[...] Publishing draft to WordPress...")
    try:
        post_id, _, edit_url = publish_draft(
            p["title"], p["slug"], p["meta_description"], p["full_draft"], p["faq_schema"]
        )
        print(f"[OK] Draft created (ID: {post_id})")
        print(f"     Edit: {edit_url}")
    except Exception as e:
        print(f"[ERROR] WordPress publish failed: {e}")

    print("\n" + "=" * 60)
    print("  PIPELINE COMPLETE")
    print("=" * 60)
    print(f"  Title:    {p['title']}")
    print(f"  Slug:     {p['slug']}")
    if drive_link:
        print(f"  Drive:    {drive_link}")
    if edit_url:
        print(f"  WP Draft: {edit_url}")
    print("\n  NEXT STEPS:")
    print("  1. Review draft in Google Drive")
    print("  2. Run Canva image creation in Claude Code")
    print("  3. Upload images to WordPress media library")
    print("  4. Set featured image + resolve internal links")
    print("  5. Publish")
    print("=" * 60)


if __name__ == "__main__":
    main()
