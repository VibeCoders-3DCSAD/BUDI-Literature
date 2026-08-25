#!/usr/bin/env python3
"""
pdf_page_filter.py - List PDFs with page counts, with optional filtering.
All pypdf logging is suppressed; only final filtered results are printed.
"""

import argparse
import logging
import sys
from pathlib import Path

# Suppress all logging from pypdf (this kills the "Ignoring..." messages)
logging.getLogger("pypdf").setLevel(logging.ERROR)

try:
    from pypdf import PdfReader
except ImportError:
    print("Error: 'pypdf' library is required. Install with: pip install pypdf", file=sys.stderr)
    sys.exit(1)


def get_pdf_page_count(pdf_path):
    """Return the number of pages in the PDF, or None if the file is invalid."""
    try:
        reader = PdfReader(pdf_path)
        return len(reader.pages)
    except Exception:
        # Silently skip corrupted/unreadable PDFs
        return None


def find_pdfs(directories):
    """Yield all PDF file paths found recursively in the given directories."""
    for directory in directories:
        root = Path(directory)
        if not root.is_dir():
            print(f"Warning: {directory} is not a directory, skipping", file=sys.stderr)
            continue
        for file_path in root.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() == ".pdf":
                yield file_path


def main():
    parser = argparse.ArgumentParser(
        description="List PDFs with page counts, with optional filters."
    )
    parser.add_argument(
        "directories",
        nargs="+",
        help="One or more directories to search for PDFs",
    )
    parser.add_argument(
        "--lte",
        type=int,
        metavar="N",
        help="Only show PDFs with page count <= N",
    )
    parser.add_argument(
        "--gte",
        type=int,
        metavar="N",
        help="Only show PDFs with page count >= N",
    )
    parser.add_argument(
        "--sort",
        choices=["name", "pages"],
        default="name",
        help="Sort output by filename (name) or page count (pages)",
    )
    args = parser.parse_args()

    matches = []  # collect (path, page_count) tuples

    for pdf_path in find_pdfs(args.directories):
        page_count = get_pdf_page_count(pdf_path)
        if page_count is None:
            continue  # skip unreadable PDFs silently

        # Apply filters
        if args.lte is not None and page_count > args.lte:
            continue
        if args.gte is not None and page_count < args.gte:
            continue

        matches.append((pdf_path, page_count))

    # Sort if requested
    if args.sort == "pages":
        matches.sort(key=lambda x: x[1])  # by page count
    else:  # name
        matches.sort(key=lambda x: str(x[0]))  # by full path

    # Display results
    if matches:
        for path, count in matches:
            print(f"{path}: {count}")
    else:
        print("No PDFs matched the given criteria.", file=sys.stderr)


if __name__ == "__main__":
    main()