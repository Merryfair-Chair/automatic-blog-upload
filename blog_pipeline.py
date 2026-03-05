import os
import re
import sys
import time
import shutil
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")
from wp_publisher import publish_draft
from drive_uploader import upload_blog

OUTPUT_DIR = Path(__file__).parent / "output"
DONE_DIR   = OUTPUT_DIR / "done"


def watch_for_file():
    """Watch output/ folder for a new .md file and return its path."""
    print("\n" + "=" * 60)
    print("  SEO BLOG PIPELINE — Waiting for Claude output")
    print("=" * 60)
    print(f"\n  Drop your Claude Phase 5 output (.md file) into:")
    print(f"  {OUTPUT_DIR}")
    print("\n  Watching... (Ctrl+C to cancel)\n")

    seen = set(OUTPUT_DIR.glob("*.md"))

    while True:
        current = set(OUTPUT_DIR.glob("*.md"))
        new_files = current - seen
        if new_files:
            new_file = sorted(new_files, key=lambda f: f.stat().st_mtime)[-1]
            print(f"[OK] Detected: {new_file.name}")
            time.sleep(1)  # Brief pause to ensure file is fully written
            return new_file
        time.sleep(2)


def parse_response(text):
    """Parse Claude's Phase 5 output into structured components."""
    def extract_section(n, nxt=None):
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

    title  = extract_section(2, 3).strip("* \n")
    meta   = extract_section(3, 4).strip("* \n")
    slug   = extract_section(4, 5).strip("` \n")
    draft  = extract_section(6, 7)
    faq_s  = extract_section(7, 8)
    fm = re.search(r'(<script type="application/ld\+json">.*?</script>)', faq_s, re.DOTALL)

    if not title:
        raise ValueError("Could not parse Title from output. Make sure you copied the full Phase 5 output.")

    return {
        "title":            title,
        "meta_description": meta,
        "slug":             slug,
        "full_draft":       draft,
        "faq_schema":       fm.group(1) if fm else "",
    }


def move_to_done(file_path, title):
    """Move processed file to output/done/ with title prefix."""
    safe_title = re.sub(r'[<>:"/\\|?*]', '-', title)[:50]
    dest = DONE_DIR / f"{safe_title} -- {file_path.name}"
    shutil.move(str(file_path), str(dest))
    print(f"[OK] Moved to done: {dest.name}")


def main():
    # Step 1: Watch for file
    md_file = watch_for_file()

    # Step 2: Read and parse
    print("\n[...] Parsing Claude output...")
    text = md_file.read_text(encoding="utf-8")
    try:
        p = parse_response(text)
    except ValueError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    print(f"[OK] Title:  {p['title']}")
    print(f"[OK] Slug:   {p['slug']}")
    print(f"[OK] FAQ schema: {'Found' if p['faq_schema'] else 'Not found'}")

    # Step 3: Save to Google Drive
    drive_link = None
    print("\n[...] Saving to Google Drive...")
    try:
        drive_link, fname = upload_blog(p["title"], p["full_draft"], p["faq_schema"])
        print(f"[OK] Saved: {fname}")
        print(f"     {drive_link}")
    except Exception as e:
        print(f"[WARN] Drive upload failed: {e}")

    # Step 4: Publish to WordPress as Draft
    edit_url = ""
    print("\n[...] Publishing draft to WordPress...")
    try:
        post_id, _, edit_url = publish_draft(
            p["title"], p["slug"], p["meta_description"], p["full_draft"], p["faq_schema"]
        )
        print(f"[OK] Draft created (ID: {post_id})")
        print(f"     Edit: {edit_url}")
    except Exception as e:
        print(f"[ERROR] WordPress publish failed: {e}")

    # Step 5: Move file to done
    move_to_done(md_file, p["title"])

    # Summary
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
