"""Validate the static template using only Python's standard library."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.ids = set()
        self.links = []
        self.errors = []

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append(f"duplicate id: {attrs['id']}")
            self.ids.add(attrs["id"])
        for attr in ("href", "src"):
            if attr in attrs:
                self.links.append(attrs[attr])
        if tag == "img":
            for attr in ("alt", "width", "height"):
                if attr not in attrs:
                    self.errors.append(f"image is missing {attr}")


def check():
    documents = {}
    failures = []
    for path in ROOT.rglob("*.html"):
        if any(part in {".git", "node_modules", "_local"} for part in path.relative_to(ROOT).parts):
            continue
        document = Document(path)
        document.feed(path.read_text(encoding="utf-8"))
        documents[path] = document
        failures.extend(f"{path.relative_to(ROOT)}: {error}" for error in document.errors)

    svg_ids = {}
    for path in (ROOT / "assets").rglob("*.svg"):
        try:
            svg_ids[path] = {element.attrib["id"] for element in ET.parse(path).iter() if "id" in element.attrib}
        except ET.ParseError as error:
            failures.append(f"{path.relative_to(ROOT)}: invalid SVG: {error}")

    for path, document in documents.items():
        for link in document.links:
            label = f"{path.relative_to(ROOT)}: {link!r}"
            if not link or link == "#":
                failures.append(f"{label}: empty destination")
                continue
            parsed = urlsplit(link)
            if parsed.scheme in {"https", "http", "mailto", "tel"}:
                continue
            if parsed.scheme or parsed.netloc or parsed.path.startswith("/"):
                failures.append(f"{label}: use a document-relative local path or an explicit https URL")
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(ROOT):
                failures.append(f"{label}: path escapes the repository")
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                failures.append(f"{label}: missing file")
                continue
            if parsed.fragment:
                ids = documents[target].ids if target in documents else svg_ids.get(target)
                if ids is not None and unquote(parsed.fragment) not in ids:
                    failures.append(f"{label}: missing fragment target")

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"PASS: {len(documents)} HTML pages, {len(svg_ids)} SVG files, local links, fragments, and image attributes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(check())
