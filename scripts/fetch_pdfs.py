#!/usr/bin/env python3
"""
Fetch PDFs from a local directory or remote source into literature/papers/.

Usage:
    # From a sibling directory containing PDFs:
    python3 scripts/fetch_pdfs.py --source local --path ../Odin-Paper/literature/papers/

    # From a directory containing .zip archives:
    python3 scripts/fetch_pdfs.py --source local --path /path/to/pdf-archives/

    # From a remote URL (must serve a .zip file):
    python3 scripts/fetch_pdfs.py --source remote --url https://example.com/papers.zip

PDFs are placed in literature/papers/ (gitignored). SHA-256 hashes are printed
for each fetched file to support frontmatter metadata in downstream conversion.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = REPO_ROOT / "literature" / "papers"


def compute_sha256(file_path: Path) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch_from_local(source_dir: Path, output_dir: Path) -> dict:
    """Copy PDFs from source_dir, or extract .zip files found in source_dir."""
    stats = {"pdfs_copied": 0, "pdfs_skipped": 0, "zips_extracted": 0, "errors": []}

    # Check if source_dir itself contains PDFs
    pdf_files = sorted(source_dir.glob("*.pdf"))
    if pdf_files:
        for pdf in pdf_files:
            dest = output_dir / pdf.name
            if dest.exists():
                print(f"  skip (exists): {pdf.name}")
                stats["pdfs_skipped"] += 1
                continue
            shutil.copy2(pdf, dest)
            sha = compute_sha256(dest)
            size_mb = dest.stat().st_size / 1_048_576
            print(f"  copied: {pdf.name} ({size_mb:.1f} MB) sha256={sha[:16]}...")
            stats["pdfs_copied"] += 1
        return stats

    # Otherwise, look for .zip files and extract PDFs from them
    zip_files = sorted(source_dir.glob("*.zip"))
    if not zip_files:
        print(f"  No PDFs or .zip files found in {source_dir}", file=sys.stderr)
        return stats

    for zf in zip_files:
        print(f"  extracting: {zf.name}")
        stats["zips_extracted"] += 1
        try:
            with zipfile.ZipFile(zf, "r") as z:
                for entry in z.namelist():
                    if not entry.lower().endswith(".pdf"):
                        continue
                    # Use just the filename, not nested paths
                    pdf_name = Path(entry).name
                    dest = output_dir / pdf_name
                    if dest.exists():
                        print(f"    skip (exists): {pdf_name}")
                        stats["pdfs_skipped"] += 1
                        continue
                    # Extract to a temp path first, then move
                    with z.open(entry) as src, open(dest, "wb") as dst:
                        shutil.copyfileobj(src, dst)
                    sha = compute_sha256(dest)
                    size_mb = dest.stat().st_size / 1_048_576
                    print(f"    extracted: {pdf_name} ({size_mb:.1f} MB) sha256={sha[:16]}...")
                    stats["pdfs_copied"] += 1
        except zipfile.BadZipFile as e:
            stats["errors"].append(f"{zf.name}: {e}")
            print(f"  ERROR: {zf.name}: {e}", file=sys.stderr)

    return stats


def fetch_from_remote(url: str, output_dir: Path) -> dict:
    """Download a .zip from a URL and extract PDFs."""
    import io
    import urllib.request

    stats = {"pdfs_copied": 0, "pdfs_skipped": 0, "errors": []}

    print(f"  downloading: {url}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Literature-Pipeline/1.0"})
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = resp.read()
    except Exception as e:
        stats["errors"].append(f"download failed: {e}")
        print(f"  ERROR: {e}", file=sys.stderr)
        return stats

    print(f"  downloaded {len(data) / 1_048_576:.1f} MB, extracting PDFs...")
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for entry in z.namelist():
                if not entry.lower().endswith(".pdf"):
                    continue
                pdf_name = Path(entry).name
                dest = output_dir / pdf_name
                if dest.exists():
                    print(f"  skip (exists): {pdf_name}")
                    stats["pdfs_skipped"] += 1
                    continue
                with z.open(entry) as src, open(dest, "wb") as dst:
                    shutil.copyfileobj(src, dst)
                sha = compute_sha256(dest)
                size_mb = dest.stat().st_size / 1_048_576
                print(f"  extracted: {pdf_name} ({size_mb:.1f} MB) sha256={sha[:16]}...")
                stats["pdfs_copied"] += 1
    except zipfile.BadZipFile as e:
        stats["errors"].append(f"invalid zip: {e}")
        print(f"  ERROR: {e}", file=sys.stderr)

    return stats


def main() -> None:
    ap = argparse.ArgumentParser(description="Fetch PDFs into literature/papers/.")
    ap.add_argument(
        "--source",
        choices=["local", "remote"],
        required=True,
        help="Local directory or remote URL",
    )
    ap.add_argument(
        "--path",
        dest="local_path",
        help="Local directory containing PDFs or .zip archives",
    )
    ap.add_argument(
        "--url",
        help="Remote URL to a .zip file",
    )
    ap.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help=f"Output directory (default: {DEFAULT_OUTPUT})",
    )
    args = ap.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.source == "local":
        if not args.local_path:
            ap.error("--path is required for --source local")
        source = Path(args.local_path)
        if not source.is_dir():
            print(f"ERROR: {source} is not a directory", file=sys.stderr)
            sys.exit(1)
        print(f"Fetching PDFs from local: {source}")
        stats = fetch_from_local(source, output_dir)
    else:
        if not args.url:
            ap.error("--url is required for --source remote")
        print(f"Fetching PDFs from remote: {args.url}")
        stats = fetch_from_remote(args.url, output_dir)

    print(f"\nDone: {stats['pdfs_copied']} fetched, {stats['pdfs_skipped']} skipped (already exist)")
    if stats.get("zips_extracted"):
        print(f"  {stats['zips_extracted']} .zip archive(s) extracted")
    if stats.get("errors"):
        print(f"  {len(stats['errors'])} error(s):")
        for err in stats["errors"]:
            print(f"    - {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
