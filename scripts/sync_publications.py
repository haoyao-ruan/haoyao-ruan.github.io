#!/usr/bin/env python3
"""Add publications that OpenAlex lists for the author but _publications/ lacks.

Existing files are never modified, so manual edits always win.
Usage: python3 scripts/sync_publications.py [--dry-run]
"""

import json
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

AUTHOR_ID = "A5005850573"
PUBLICATIONS_DIR = Path(__file__).resolve().parent.parent / "_publications"
API_URL = (
    "https://api.openalex.org/works"
    f"?filter=author.id:{AUTHOR_ID}&per-page=200&sort=publication_date:desc"
)

# Works that should stay off the site even though OpenAlex lists them.
SKIP_DOIS = {
    "10.1121/10.0040967",  # JASA 2025 meeting abstract, not on the CV
}

LINGUISTICS_VENUE = re.compile(r"speech|phon|acoust|linguist|language|prosody", re.I)
MAX_AUTHORS_IN_FULL = 7


def normalize_title(title):
    text = unicodedata.normalize("NFKD", title).lower()
    return re.sub(r"[^a-z0-9]", "", text)


def bare_doi(doi):
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", doi or "").lower()


def existing_keys():
    dois, titles = set(), set()
    for path in PUBLICATIONS_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        doi = re.search(r"^doi:\s*['\"]?([^'\"\n]+)", text, re.M)
        if doi:
            dois.add(bare_doi(doi.group(1).strip()))
        title = re.search(r"^title:\s*(.+)$", text, re.M)
        if title:
            titles.add(normalize_title(title.group(1)))
    return dois, titles


def short_name(display_name):
    """'Dawn Marie Behne' -> 'Behne DM'; 'Sophie van Beekhuizen' -> 'van Beekhuizen S'."""
    parts = display_name.replace(".", "").split()
    if len(parts) == 1:
        return parts[0]
    start = len(parts) - 1
    while start > 1 and parts[start - 1][0].islower():
        start -= 1
    initials = "".join(p[0] for p in parts[:start])
    return f"{' '.join(parts[start:])} {initials}"


def is_me(authorship):
    return (authorship["author"].get("id") or "").endswith(AUTHOR_ID)


def author_line(work):
    names, mine = [], None
    for authorship in work["authorships"]:
        name = short_name(authorship["author"]["display_name"])
        if is_me(authorship):
            name = mine = f"<b>{name}</b>"
        names.append(name)
    if len(names) <= MAX_AUTHORS_IN_FULL:
        return ", ".join(names)
    lead = names[:3]
    if mine is None or mine in lead:
        return ", ".join(lead) + ", et al."
    return ", ".join(lead) + f", et al., including {mine}"


def venue_line(work):
    source = ((work.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
    biblio = work.get("biblio") or {}
    parts = [source]
    if biblio.get("volume"):
        issue = f"({biblio['issue']})" if biblio.get("issue") else ""
        parts.append(f"{biblio['volume']}{issue}")
    first, last = biblio.get("first_page"), biblio.get("last_page")
    if first:
        parts.append(first if not last or last == first else f"{first}–{last}")
    return ", ".join(p for p in parts if p)


def category(work, venue):
    if "abstract" in (work.get("type") or ""):
        return "abstracts"
    if LINGUISTICS_VENUE.search(venue):
        return "linguistics"
    first_author_is_me = bool(work["authorships"]) and is_me(work["authorships"][0])
    return "methods" if first_author_is_me else "pharma"


def slugify(title):
    text = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
    words = re.findall(r"[a-z0-9]+", text)
    return "-".join(words[:6])


def render(work):
    title = work["title"].strip()
    date = work["publication_date"]
    venue = venue_line(work)
    section = category(work, venue)
    authors = author_line(work)
    if section == "linguistics":
        authors = re.sub(r"</?b>", "", authors)
    stem = f"{date}-{slugify(title)}"
    citation = f"{authors} ({date[:4]}). {title}. <i>{venue}</i>."
    quote = lambda value: json.dumps(value, ensure_ascii=False)
    body = "\n".join([
        "---",
        f"title: {quote(title)}",
        "collection: publications",
        f"category: {section}",
        f"permalink: /publication/{stem}",
        f"date: {date}",
        f"authors: {quote(authors)}",
        f"venue: {quote(venue)}",
        f"doi: {quote(bare_doi(work['doi']))}",
        f"citation: {quote(citation)}",
        "---",
        "",
    ])
    return stem, body


def fetch_works():
    request = urllib.request.Request(API_URL, headers={"User-Agent": "academicpages-publication-sync"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)["results"]


def main():
    dry_run = "--dry-run" in sys.argv
    dois, titles = existing_keys()
    added = 0
    for work in fetch_works():
        doi = bare_doi(work.get("doi"))
        title = work.get("title") or ""
        if not doi or not title or doi in SKIP_DOIS:
            continue
        if doi in dois or normalize_title(title) in titles:
            continue
        stem, body = render(work)
        print(f"{'Would add' if dry_run else 'Added'}: {stem}.md")
        if not dry_run:
            (PUBLICATIONS_DIR / f"{stem}.md").write_text(body, encoding="utf-8")
        added += 1
    print(f"{added} new publication(s).")


if __name__ == "__main__":
    main()
