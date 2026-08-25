#!/usr/bin/env python3
"""
PDF to Markdown Converter with Metadata and Page-Aware Extraction

Usage: python3 prepare_pdf.py [target_directory]

Scans the target directory for PDF files, converts each to Markdown via
MarkItDown, adds YAML frontmatter with conversion metadata, optionally
extracts page-aware text with paragraph detection via pdfminer.six,
and creates empty summary placeholder files.
"""

import argparse
import hashlib
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from markitdown import MarkItDown
except ImportError:
    raise ImportError(
        "The 'markitdown' package is required. Install it with: pip install markitdown"
    )

try:
    from pypdf import PdfReader

    PYPDF_AVAILABLE = True
except ImportError:
    PYPDF_AVAILABLE = False

try:
    from pdfminer.high_level import extract_pages
    from pdfminer.layout import LAParams, LTTextBox

    PDFMINER_AVAILABLE = True
except ImportError:
    PDFMINER_AVAILABLE = False


def compute_sha256(file_path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def get_pdf_page_count(pdf_path: Path) -> int | None:
    """Return the number of pages in the PDF, or None if unreadable."""
    if not PYPDF_AVAILABLE:
        return None
    try:
        reader = PdfReader(str(pdf_path))
        return len(reader.pages)
    except Exception:
        return None


def extract_paragraphs_per_page(pdf_path: Path) -> list[list[str]]:
    """Extract paragraph blocks from each page using pdfminer.six.

    Returns a list of pages, where each page is a list of paragraph strings.
    Paragraphs are determined by LTTextBox grouping (LAParams line_margin=0.5).
    """
    if not PDFMINER_AVAILABLE:
        return []
    try:
        laparams = LAParams(line_margin=0.5)
        pages = []
        for page_layout in extract_pages(str(pdf_path), laparams=laparams):
            paragraphs = []
            for element in page_layout:
                if isinstance(element, LTTextBox):
                    text = element.get_text().strip()
                    if text:
                        paragraphs.append(text)
            pages.append(paragraphs)
        return pages
    except Exception:
        return []


def build_page_aware_markdown(pages: list[list[str]]) -> str:
    """Build a markdown string with page markers and paragraph separation.

    Each page is delimited by <!-- PAGE N --> markers.
    Paragraphs within a page are separated by blank lines.
    """
    parts = []
    for i, paragraphs in enumerate(pages, 1):
        if paragraphs:
            page_text = "\n\n".join(paragraphs)
            parts.append(f"<!-- PAGE {i} -->\n\n{page_text}")
    return "\n\n---\n\n".join(parts)


def build_frontmatter(
    pdf_path: Path,
    md_char_count: int,
    page_count: int | None,
    converter_version: str,
) -> str:
    """Build YAML frontmatter block with conversion metadata."""
    now = datetime.now(timezone.utc).isoformat(timespec="seconds").replace(
        "+00:00", "Z"
    )
    pdf_hash = compute_sha256(pdf_path)

    lines = [
        "---",
        "conversion_metadata:",
        f'  converted_at: "{now}"',
        f'  converter_tool: "markitdown"',
        f'  converter_version: "{converter_version}"',
        f'  source_pdf: "{pdf_path.name}"',
        f'  source_pdf_sha256: "{pdf_hash}"',
    ]
    if page_count is not None:
        lines.append(f"  page_count: {page_count}")
    else:
        lines.append("  page_count: null")
    lines.append(f"  markdown_char_count: {md_char_count}")
    lines.append("---")
    return "\n".join(lines)


def get_markitdown_version() -> str:
    """Best-effort extraction of markitdown version."""
    try:
        import importlib.metadata

        return importlib.metadata.version("markitdown")
    except Exception:
        return "unknown"


def find_pdfs(directory: Path) -> list[Path]:
    """Return a list of PDF file paths in the given directory."""
    return sorted(directory.glob("*.pdf"))


def convert_pdf_to_markdown(pdf_path: Path) -> str:
    """Convert a PDF file to Markdown using MarkItDown. Returns the text content."""
    md_converter = MarkItDown()
    result = md_converter.convert(str(pdf_path))
    return result.text_content


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF files to Markdown with metadata and optional page-aware extraction."
    )
    parser.add_argument(
        "target_dir",
        nargs="?",
        default=".",
        help="Directory containing PDF files (default: current directory)",
    )
    parser.add_argument(
        "--suffix",
        default="_marked.md",
        help="Suffix for the converted Markdown file (default: '_marked.md')",
    )
    parser.add_argument(
        "--summary-suffix",
        default="_summarized.json",
        help="Suffix for the empty summary file (default: '_summarized.json')",
    )
    parser.add_argument(
        "--no-summary",
        action="store_true",
        help="Do not create empty summary files",
    )
    parser.add_argument(
        "--no-frontmatter",
        action="store_true",
        help="Do not add YAML frontmatter to the markdown output",
    )
    parser.add_argument(
        "--page-aware",
        action="store_true",
        help="Add page markers (<!-- PAGE N -->) with paragraph detection via pdfminer.six",
    )
    parser.add_argument(
        "--json-sidecar",
        action="store_true",
        help="Write a separate {stem}_conversion_meta.json alongside the markdown",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    target_dir = Path(args.target_dir).resolve()
    if not target_dir.is_dir():
        logging.error(f"'{target_dir}' is not a valid directory.")
        sys.exit(1)

    pdf_files = find_pdfs(target_dir)
    if not pdf_files:
        logging.info(f"No PDF files found in '{target_dir}'.")
        return

    logging.info(f"Found {len(pdf_files)} PDF file(s) in '{target_dir}'.")
    if args.page_aware and not PDFMINER_AVAILABLE:
        logging.warning(
            "--page-aware requires pdfminer.six. Page markers will be skipped. "
            "Install with: pip install pdfminer.six"
        )

    converter_version = get_markitdown_version()
    success_count = 0

    for idx, pdf_path in enumerate(pdf_files, start=1):
        stem = pdf_path.stem
        marked_path = target_dir / f"{stem}{args.suffix}"
        summary_path = target_dir / f"{stem}{args.summary_suffix}"
        sidecar_path = target_dir / f"{stem}_conversion_meta.json"

        logging.info(f"[{idx}/{len(pdf_files)}] Converting: {pdf_path.name}")

        try:
            # Get page count
            page_count = get_pdf_page_count(pdf_path)
            if page_count is not None:
                logging.debug(f"  -> Page count: {page_count}")

            # Convert with MarkItDown
            md_content = convert_pdf_to_markdown(pdf_path)

            # Optionally add page markers with paragraph detection
            if args.page_aware and PDFMINER_AVAILABLE:
                pages = extract_paragraphs_per_page(pdf_path)
                if pages:
                    page_md = build_page_aware_markdown(pages)
                    # Prepend page-aware version as a reference section
                    md_content = (
                        f"<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->\n\n"
                        f"{page_md}\n\n"
                        f"<!-- MARKITDOWN CONVERSION -->\n\n"
                        f"<!-- The following is the full MarkItDown conversion "
                        f"for formatting fidelity. -->\n\n"
                        f"{md_content}"
                    )

            # Add frontmatter
            if not args.no_frontmatter:
                frontmatter = build_frontmatter(
                    pdf_path,
                    md_char_count=len(md_content),
                    page_count=page_count,
                    converter_version=converter_version,
                )
                md_content = f"{frontmatter}\n\n{md_content}"

            # Write markdown
            marked_path.write_text(md_content, encoding="utf-8")
            logging.debug(f"  -> Created {marked_path.name}")

            # Write JSON sidecar if requested
            if args.json_sidecar:
                sidecar = {
                    "converted_at": datetime.now(timezone.utc)
                    .isoformat(timespec="seconds")
                    .replace("+00:00", "Z"),
                    "converter_tool": "markitdown",
                    "converter_version": converter_version,
                    "source_pdf": pdf_path.name,
                    "source_pdf_sha256": compute_sha256(pdf_path),
                    "page_count": page_count,
                    "markdown_char_count": len(md_content),
                    "output_file": marked_path.name,
                }
                sidecar_path.write_text(
                    json.dumps(sidecar, indent=2) + "\n", encoding="utf-8"
                )
                logging.debug(f"  -> Created {sidecar_path.name}")

        except Exception as e:
            logging.error(f"  Failed to convert {pdf_path.name}: {e}")
            continue

        if not args.no_summary:
            summary_path.touch()
            logging.debug(f"  -> Created empty summary {summary_path.name}")

        success_count += 1

    logging.info(f"Successfully processed {success_count} of {len(pdf_files)} PDF(s).")


if __name__ == "__main__":
    main()
