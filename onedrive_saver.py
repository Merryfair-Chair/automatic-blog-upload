"""
Save each new blog draft as a Word file in OneDrive → "Blog Post Material".

Replaces drive_uploader.py: Google Workspace was shut off on 2026-09-28 (move to
Microsoft 365), so the Google Drive copy can no longer be written.

How it works: the file is written into the OneDrive folder that the OneDrive app
syncs on this Mac; the app uploads it. No Microsoft login, API key or IT approval
is involved. The target ACCOUNT is the company marketing@ OneDrive — the folder is
looked up in the OneDrive app's own settings, so a file can never land in a
different account or in a folder that is not actually synced.

Settings (optional, in .env):
  ONEDRIVE_ACCOUNT      default "marketing_merryfair_com"  (part of the account's web address)
  ONEDRIVE_BLOG_FOLDER  default "Blog Post Material"
  ONEDRIVE_ROOT         testing only: write into this folder instead of OneDrive

Same interface as drive_uploader:  upload_blog(title, markdown, faq_schema) -> (link, file_name)
"""

import json
import os
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote

import markdown as md_lib
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

ACCOUNT = os.environ.get("ONEDRIVE_ACCOUNT", "marketing_merryfair_com")
FOLDER_NAME = os.environ.get("ONEDRIVE_BLOG_FOLDER", "Blog Post Material")

BODY_FONT, BODY_SIZE = "Arial", 11
MONO_FONT, MONO_SIZE = "Courier New", 9


# ───────────────────────── where to save ─────────────────────────

def _finder_folder(scope_line):
    """
    The folder Finder shows for an account (~/Library/CloudStorage/OneDrive-…), matched by the
    sync id the app keeps in a hidden file at that folder's root. The app's internal copy
    (Group Container) turns into empty placeholders once uploaded, so it cannot be read back.
    """
    for root in (Path.home() / "Library/CloudStorage").glob("OneDrive-*"):
        for marker in root.glob(".*-*-*-*-*"):
            try:
                guid = json.loads(marker.read_text()).get("guid", "")
            except (OSError, ValueError, AttributeError):
                continue
            if guid and guid in scope_line:
                return root
    return None


def _finder_folder_by_name(sync_root):
    """
    The same folder found by its name: 'OneDrive - Company Name' is shown in Finder as
    'OneDrive-CompanyName'. Needed when this runs as a background program: macOS then does not
    let it look inside OneDrive folders (so the sync id cannot be read), only add new files.
    """
    name = Path(sync_root).name
    if not name.startswith("OneDrive"):
        return None
    folder = Path.home() / "Library/CloudStorage" / name.replace(" ", "")
    return folder if folder.is_dir() else None


def onedrive_accounts():
    """{account web address: local synced folder} for accounts the OneDrive app is syncing."""
    settings = Path.home() / "Library/Application Support/OneDrive/settings"
    containers = [Path.home() / "Library/Group Containers" / n
                  for n in ("UBF8T346G9.OneDriveStandaloneSuite", "UBF8T346G9.OneDriveSyncClientSuite")]
    found = {}
    for ini in settings.glob("Business*/*.ini"):
        raw = ini.read_bytes()
        text = raw.decode("utf-16" if raw[:2] in (b"\xff\xfe", b"\xfe\xff") else "utf-8", errors="ignore")
        for line in text.splitlines():
            if not line.startswith("libraryScope"):
                continue
            quoted = re.findall(r'"([^"]*)"', line)
            url = next((q for q in quoted if q.startswith("https://") and "/personal/" in q), None)
            local = next((q for q in quoted if q.startswith("$Group.Container$") or q.startswith("/")), None)
            if not url or not local:
                continue
            finder = _finder_folder(line)
            if finder:
                found[url.rstrip("/")] = finder
                continue
            if local.startswith("$Group.Container$"):
                rel = local[len("$Group.Container$"):].lstrip("/")
                local = next((str(c / rel) for c in containers if (c / rel).is_dir()), "")
                local = str(_finder_folder_by_name(local) or local) if local else ""
            if local and Path(local).is_dir():
                found[url.rstrip("/")] = Path(local)
    return found


def target_folder():
    """(local folder to write into, web address of that folder or None)."""
    if os.environ.get("ONEDRIVE_ROOT"):                       # testing
        folder = Path(os.environ["ONEDRIVE_ROOT"]) / FOLDER_NAME
        folder.mkdir(parents=True, exist_ok=True)
        return folder, None
    for url, local in onedrive_accounts().items():
        if ACCOUNT in url:
            folder = local / FOLDER_NAME
            folder.mkdir(exist_ok=True)
            return folder, f"{url}/Documents/{quote(FOLDER_NAME)}"
    raise RuntimeError(
        f"OneDrive is not syncing the account '{ACCOUNT}' on this Mac, so the Word copy was not saved. "
        "Open the OneDrive app, sign in to that account and let it finish setting up."
    )


# ───────────────────────── Markdown → Word ─────────────────────────

def _style_run(run, bold=False, italic=False, mono=False):
    run.font.name = MONO_FONT if mono else BODY_FONT
    run.font.size = Pt(MONO_SIZE if mono else BODY_SIZE)
    run.bold = bold or None
    run.italic = italic or None


def _add_link(par, url, text, bold=False, italic=False):
    r_id = par.part.relate_to(url, RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    r, rpr = OxmlElement("w:r"), OxmlElement("w:rPr")
    fonts = OxmlElement("w:rFonts")
    fonts.set(qn("w:ascii"), BODY_FONT)
    fonts.set(qn("w:hAnsi"), BODY_FONT)
    rpr.append(fonts)
    if bold:
        rpr.append(OxmlElement("w:b"))
    if italic:
        rpr.append(OxmlElement("w:i"))
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    rpr.append(color)
    size = OxmlElement("w:sz")
    size.set(qn("w:val"), str(BODY_SIZE * 2))
    rpr.append(size)
    under = OxmlElement("w:u")
    under.set(qn("w:val"), "single")
    rpr.append(under)
    r.append(rpr)
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = text
    r.append(t)
    link.append(r)
    par._p.append(link)


class _WordBuilder(HTMLParser):
    """Turns the HTML that the `markdown` library produces into Word paragraphs."""

    HEADINGS = {"h1": 1, "h2": 2, "h3": 3, "h4": 4, "h5": 5, "h6": 6}

    def __init__(self, doc):
        super().__init__(convert_charrefs=True)
        self.doc = doc
        self.par = None            # paragraph being written
        self.inline = []           # open inline tags: strong / em / code
        self.href = None
        self.lists = []            # open lists: ["ul"] or ["ol", next_number]
        self.quote = 0
        self.pre = False
        self.heading = False
        self.skip = 0              # inside <script>/<style>
        self.rows = None           # table being collected: list of rows of cells of tokens
        self.cell = None

    # -- helpers --
    def _new_par(self, style=None):
        self.par = self.doc.add_paragraph(style=style)
        if self.quote and not style:
            self.par.paragraph_format.left_indent = Inches(0.4)
        return self.par

    def _write(self, par, tok):
        text, bold, italic, mono, href = tok
        if href:
            _add_link(par, href, text, bold, italic)
        else:
            _style_run(par.add_run(text), bold, italic, mono)

    def _emit(self, text):
        tok = (text, "strong" in self.inline or self.heading and False, "em" in self.inline or bool(self.quote),
               "code" in self.inline, self.href)
        if self.cell is not None:
            self.cell.append(tok)
            return
        if self.par is None:
            self._new_par()
        if self.heading:                       # headings keep Word's own heading look
            run = self.par.add_run(text)
            run.font.name = BODY_FONT
        else:
            self._write(self.par, tok)

    # -- parser events --
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        elif tag in self.HEADINGS:
            self._new_par(style=f"Heading {self.HEADINGS[tag]}")
            self.heading = True
        elif tag == "p":
            if self.cell is None and not (self.lists and self.par is not None and not self.par.text):
                self._new_par()
        elif tag in ("ul", "ol"):
            self.lists.append([tag, 1])
        elif tag == "li":
            depth = len(self.lists)
            kind = self.lists[-1] if self.lists else ["ul", 1]
            if kind[0] == "ul":
                self._new_par(style="List Bullet" if depth <= 1 else "List Bullet 2")
            else:                               # explicit numbers: Word's auto-numbering never restarts
                self._new_par()
                self.par.paragraph_format.left_indent = Inches(0.25 * depth + 0.1)
                self.par.paragraph_format.first_line_indent = Inches(-0.25)
                _style_run(self.par.add_run(f"{kind[1]}. "))
                kind[1] += 1
        elif tag == "blockquote":
            self.quote += 1
        elif tag == "pre":
            self.pre = True
            self.par = None
        elif tag in ("strong", "b"):
            self.inline.append("strong")
        elif tag in ("em", "i"):
            self.inline.append("em")
        elif tag == "code":
            self.inline.append("code")
        elif tag == "a":
            self.href = dict(attrs).get("href") or None
        elif tag == "br":
            if self.cell is not None:
                self.cell.append((" ", False, False, False, None))
            elif self.par is not None:
                self.par.add_run().add_break()
        elif tag == "hr":
            _style_run(self._new_par().add_run("— — —"))
            self.par = None
        elif tag == "table":
            self.rows = []
        elif tag == "tr" and self.rows is not None:
            self.rows.append([])
        elif tag in ("th", "td") and self.rows:
            self.cell = []
            self.rows[-1].append((tag == "th", self.cell))

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        elif tag in self.HEADINGS:
            self.heading = False
            self.par = None
        elif tag in ("p", "li"):
            if self.cell is None:
                self.par = None
        elif tag in ("ul", "ol"):
            if self.lists:
                self.lists.pop()
            self.par = None
        elif tag == "blockquote":
            self.quote = max(0, self.quote - 1)
        elif tag == "pre":
            self.pre = False
            self.par = None
        elif tag in ("strong", "b", "em", "i", "code"):
            name = {"b": "strong", "i": "em"}.get(tag, tag)
            if name in self.inline:
                self.inline.remove(name)
        elif tag == "a":
            self.href = None
        elif tag in ("th", "td"):
            self.cell = None
        elif tag == "table" and self.rows is not None:
            self._flush_table()

    def handle_data(self, data):
        if self.skip:
            return
        if self.pre:
            for line in data.rstrip("\n").split("\n"):
                p = self.doc.add_paragraph()
                p.paragraph_format.space_after = Pt(0)
                _style_run(p.add_run(line), mono=True)
            return
        text = re.sub(r"\s+", " ", data)
        if not text.strip() and (self.par is None and self.cell is None):
            return
        if self.par is not None and not self.par.text and self.cell is None:
            text = text.lstrip()
        if text:
            self._emit(text)

    def _flush_table(self):
        rows = [r for r in self.rows if r]
        self.rows, self.cell, self.par = None, None, None
        if not rows:
            return
        table = self.doc.add_table(rows=len(rows), cols=max(len(r) for r in rows))
        table.style = "Table Grid"
        for i, row in enumerate(rows):
            for j, (is_header, tokens) in enumerate(row):
                par = table.cell(i, j).paragraphs[0]
                for text, bold, italic, mono, href in tokens:
                    self._write(par, (text, bold or is_header, italic, mono, href))
        self.doc.add_paragraph()


def markdown_to_docx(title, markdown_text, faq_schema):
    # Same readability clean-up the Google Docs version applied
    markdown_text = re.sub(r'\[IMAGE-FEATURED: ([^\]]+)\]', r'\n\n**[FEATURED IMAGE: \1]**\n\n', markdown_text)
    markdown_text = re.sub(r'\[IMAGE-CONTENT: ([^\]]+)\]',  r'\n\n**[CONTENT IMAGE: \1]**\n\n',  markdown_text)
    markdown_text = re.sub(r'\[IMAGE-DATA: ([^\]]+)\]',     r'\n\n**[MANUAL IMAGE: \1]**\n\n',    markdown_text)
    markdown_text = re.sub(r'\[QUOTABLE\]\s*', '', markdown_text)

    doc = Document()
    doc.core_properties.title = title
    normal = doc.styles["Normal"]
    normal.font.name, normal.font.size = BODY_FONT, Pt(BODY_SIZE)

    builder = _WordBuilder(doc)
    builder.feed(md_lib.markdown(markdown_text, extensions=["tables", "fenced_code"]))
    builder.close()

    if faq_schema:
        _style_run(doc.add_paragraph().add_run("— — —"))
        doc.add_paragraph("FAQ SCHEMA (Custom HTML Block)", style="Heading 2")
        for line in faq_schema.split("\n"):
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(0)
            _style_run(p.add_run(line), mono=True)
    return doc


# ───────────────────────── public API ─────────────────────────

def upload_blog(title, content, faq_schema):
    folder, web = target_folder()
    safe_title = re.sub(r'[<>:"/\\|?*]', '-', title).strip().rstrip(".")
    path = folder / f"{safe_title}.docx"
    n = 2
    while path.exists():                       # never overwrite an earlier draft
        path = folder / f"{safe_title} ({n}).docx"
        n += 1
    try:
        markdown_to_docx(title, content, faq_schema).save(str(path))
    except PermissionError:
        raise RuntimeError(
            "macOS is not letting this background program into the OneDrive folder. In System Settings → "
            "Privacy & Security, give Python access to OneDrive files, then restart the pipeline."
        )
    link = f"{web}/{quote(path.name)}?web=1" if web else str(path)
    return link, path.name


if __name__ == "__main__":
    try:
        folder, web = target_folder()
        print(f"[OK] OneDrive account '{ACCOUNT}' is syncing on this Mac")
        print(f"[OK] Drafts will be saved to: {folder}")
    except RuntimeError as e:
        print(f"[NOT READY] {e}")
        synced = list(onedrive_accounts())
        print("Accounts syncing right now:", synced or "none")
