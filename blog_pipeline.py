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


def watch_for_file(seen):
    """Watch for a new .md file and return it when found."""
    current = set(OUTPUT_DIR.glob("*.md"))
    new_files = current - seen
    if new_files:
        md_file = sorted(new_files, key=lambda f: f.stat().st_mtime)[-1]
        log(f"Detected: {md_file.name}")
        time.sleep(1)
        return md_file, current
    return None, current


def log(msg):
    """Print with timestamp."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}", flush=True)


def parse_response(text):
    """Parse Claude's Phase 5 output into structured components.

    Supports two formats:
      - Numbered: ## [2] TITLE TAG / ## [3] META DESCRIPTION / etc.
      - Named:    # TITLE TAG / # META DESCRIPTION / etc.
    """

    # ── Named-heading format (new) ─────────────────────────────────────────
    if re.search(r'^#+\s+TITLE TAG\s*$', text, re.MULTILINE | re.IGNORECASE):

        def extract_named(heading, stop_heading=None):
            m = re.search(r'^#+\s+' + re.escape(heading) + r'\s*$',
                          text, re.MULTILINE | re.IGNORECASE)
            if not m:
                return ""
            start = m.end()
            if stop_heading:
                m2 = re.search(r'^#+\s+' + re.escape(stop_heading) + r'\s*$',
                               text[start:], re.MULTILINE | re.IGNORECASE)
                end = start + m2.start() if m2 else len(text)
            else:
                end = len(text)
            return text[start:end].strip()

        raw_title = extract_named("TITLE TAG", "META DESCRIPTION")
        meta      = extract_named("META DESCRIPTION", "URL SLUG")
        raw_slug  = extract_named("URL SLUG", "SELECTED H1")
        # Full draft = everything between SELECTED H1 and FAQ SCHEMA
        draft     = extract_named("SELECTED H1", "FAQ SCHEMA")
        faq_s     = extract_named("FAQ SCHEMA")

    # ── Numbered format (original) ─────────────────────────────────────────
    else:
        def extract_section(n, nxt=None):
            m = re.search(r"(?:#+\s*\[" + str(n) + r"\][^\n]*\n|\*\*\[" + str(n) + r"\].*?\*\*)", text)
            if not m:
                return ""
            start = m.end()
            if nxt:
                m2 = re.search(r"(?:##+ \[" + str(nxt) + r"\]|\*\*\[" + str(nxt) + r"\])", text[start:])
                end = start + m2.start() if m2 else len(text)
            else:
                end = len(text)
            return text[start:end].strip()

        raw_title = extract_section(2, 3).strip("* \n")
        meta      = extract_section(3, 4).strip("* \n")
        raw_slug  = extract_section(4, 5).strip("` \n")
        draft     = extract_section(6, 7)
        faq_s     = extract_section(7, 8)

    # ── Clean shared fields ────────────────────────────────────────────────
    title = re.sub(r'\s*\([\d]+\s*chars?\)', '', raw_title).strip().strip('-').strip()
    title = next((l.strip().strip('*') for l in title.splitlines() if l.strip()), title)

    meta  = re.sub(r'\s*\([\d]+\s*chars?\)', '', meta).strip()
    meta  = next((l.strip() for l in meta.splitlines() if l.strip()), meta)

    slug  = next((l.strip().strip('`') for l in raw_slug.splitlines() if l.strip()), raw_slug)

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


def move_to_done(file_path, slug):
    """Move processed file to output/done/ renamed to slug."""
    safe_slug = re.sub(r'[<>:"/\\|?*\n\r]', '-', slug)[:80]
    dest = DONE_DIR / f"{safe_slug}.md"
    if dest.exists():
        dest = DONE_DIR / f"{safe_slug}-{int(time.time())}.md"
    shutil.move(str(file_path), str(dest))
    print(f"[OK] Moved to done: {dest.name}")


def process(md_file):
    """Process a single .md file through the full pipeline."""
    print("\n" + "=" * 60)
    print("  SEO BLOG PIPELINE")
    print("=" * 60)

    # Parse
    log("Parsing Claude output...")
    text = md_file.read_text(encoding="utf-8")
    try:
        p = parse_response(text)
    except ValueError as e:
        log(f"ERROR: {e}")
        return

    log(f"Title:  {p['title']}")
    log(f"Slug:   {p['slug']}")
    log(f"FAQ schema: {'Found' if p['faq_schema'] else 'Not found'}")

    # Google Drive
    drive_link = None
    log("Saving to Google Drive...")
    try:
        drive_link, fname = upload_blog(p["title"], p["full_draft"], p["faq_schema"])
        log(f"Saved: {fname}")
        log(f"Drive: {drive_link}")
    except Exception as e:
        log(f"WARN: Drive upload failed: {e}")

    # WordPress
    edit_url = ""
    log("Publishing draft to WordPress...")
    try:
        post_id, _, edit_url = publish_draft(p["title"], p["slug"], p["full_draft"])
        log(f"Draft created: {edit_url}")
    except Exception as e:
        log(f"ERROR: WordPress publish failed: {e}")

    # Move to done
    move_to_done(md_file, p["slug"])

    # Summary
    print("\n" + "=" * 60)
    print("  PIPELINE COMPLETE")
    print("=" * 60)
    print(f"  Title:    {p['title']}")
    if drive_link:
        print(f"  Drive:    {drive_link}")
    if edit_url:
        print(f"  WP Draft: {edit_url}")
    print("\n  NEXT STEPS (manual):")
    print("  1. Fill in Yoast SEO fields (title, slug, meta description)")
    print("  2. Paste FAQ schema into Custom Script meta box")
    print("  3. Add images + set featured image")
    print("  4. Resolve internal links")
    print("  5. Publish")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    log(f"Watcher started. Monitoring: {OUTPUT_DIR}")
    seen = set(OUTPUT_DIR.glob("*.md"))

    # Process any file already sitting in the folder
    if seen:
        for f in sorted(seen, key=lambda f: f.stat().st_mtime):
            process(f)
        seen = set(OUTPUT_DIR.glob("*.md"))

    # Loop forever watching for new files
    while True:
        md_file, seen = watch_for_file(seen)
        if md_file:
            process(md_file)
            seen = set(OUTPUT_DIR.glob("*.md"))
        time.sleep(2)
