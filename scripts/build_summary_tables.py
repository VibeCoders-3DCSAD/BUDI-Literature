#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import yaml

from common import DEFAULT_NOTES, REPO_ROOT, load_metadata, load_note


def cell(value: object, limit: int = 220) -> str:
    del limit
    return " ".join(str(value or "").split()).replace("|", "\\|")


def sentence_cell(value: object, limit: int = 220) -> str:
    del limit
    return " ".join(str(value or "").split()).replace("|", "\\|")


def module_labels() -> dict[str, str]:
    taxonomy_path = REPO_ROOT / "config" / "taxonomy.yaml"
    with taxonomy_path.open(encoding="utf-8") as handle:
        taxonomy = yaml.safe_load(handle)
    return {
        str(module["id"]): str(module["name"])
        for module in taxonomy.get("modules", [])
        if module.get("id") and module.get("name")
    }


def module_text(modules: list[str], labels: dict[str, str]) -> str:
    if not modules:
        return "Not reported"
    return ", ".join(labels.get(module, module) for module in modules)


def work(meta: dict, stem: str) -> str:
    author = str(meta.get("first_author") or stem.split("--")[-1].replace("-", " "))
    year = str(meta.get("year") or "n.d.")
    title = cell(meta.get("title") or "Not reported", 400)
    return f"{author} ({year}). {title}."


def note_finding(stem: str) -> str:
    note = load_note(DEFAULT_NOTES / (stem + ".md")) or {}
    return str(note.get("tldr") or "Not reported")


def stream(note: dict) -> str:
    return str((note.get("frontmatter") or {}).get("review_stream") or "").strip()


def build(notes_dir: Path, out_dir: Path) -> tuple[int, int]:
    meta = load_metadata()
    labels = module_labels()
    rows = []
    for path in sorted(notes_dir.glob("*.md")):
        note = load_note(path)
        if not note or note.get("status") != "extracted":
            continue
        stream_value = stream(note)
        if stream_value not in {"literature", "study"}:
            continue
        stem = path.stem
        record = meta.get(stem) or {}
        modules = module_text(note.get("modules") or [], labels)
        rows.append(
            {
                "stem": stem,
                "stream": stream_value,
                "year": str(record.get("year") or ""),
                "work": work(record, stem),
                "design": cell(note.get("study_design") or "Not reported", 140),
                "sample": cell(note.get("sample") or "Not reported", 180),
                "finding": cell(note.get("tldr") or "Not reported", 260),
                "gap": cell((note.get("limitations") or ["Not reported"])[0], 220),
                "modules": cell(modules, 400),
            }
        )
    rows.sort(key=lambda r: (r["stream"], r["year"], r["stem"]))
    literature = [r for r in rows if r["stream"] != "study"]
    studies = [r for r in rows if r["stream"] == "study"]
    out_dir.mkdir(parents=True, exist_ok=True)
    generated = date.today().isoformat()

    lit = [
        "# Related Literature",
        "",
        f"Generated {generated} from `review/notes/`. {len(literature)} extracted works are marked `review_stream: literature`.",
        "These works supply definitions, standards, context, or methods; they are not reported as primary studies in the review.",
        "",
        "| Work | Focus | Modules |",
        "| :--- | :--- | :--- |",
    ]
    for r in literature:
        lit.append(f"| {r['work']} | {r['finding']} | {r['modules']} |")
    lit.append("")
    (out_dir / "related-literature.md").write_text("\n".join(lit))

    stu = [
        "# Related Studies",
        "",
        f"Generated {generated} from `review/notes/`. {len(studies)} extracted works are marked `review_stream: study`.",
        "These works report primary data, a model, or a system evaluation and are summarized for comparison.",
        "",
        "| Study | Design | Sample | Key finding | Limitation | Modules |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for r in studies:
        stu.append(
            f"| {r['work']} | {r['design']} | {r['sample']} | {r['finding']} | {r['gap']} | {r['modules']} |"
        )
    stu.append("")
    (out_dir / "related-studies.md").write_text("\n".join(stu))

    lit_compact = [
        "# Related Literature Summary",
        "",
        "| Work | Focus | Modules |",
        "| :--- | :--- | :--- |",
    ]
    for r in literature:
        lit_compact.append(
            f"| {r['work']} | {sentence_cell(note_finding(r['stem']), 180)} | {r['modules']} |"
        )
    lit_compact.append("")
    (out_dir / "related-literature-compact.md").write_text("\n".join(lit_compact))

    stu_compact = [
        "# Related Studies Summary",
        "",
        "| Study | Key finding | Modules |",
        "| :--- | :--- | :--- |",
    ]
    for r in studies:
        stu_compact.append(
            f"| {r['work']} | {sentence_cell(r['finding'], 220)} | {cell(r['modules'], 400)} |"
        )
    stu_compact.append("")
    (out_dir / "related-studies-compact.md").write_text("\n".join(stu_compact))
    return len(literature), len(studies)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the Chapter 2 related-literature and related-studies tables.")
    parser.add_argument("--notes", type=Path, default=DEFAULT_NOTES)
    parser.add_argument("--out", type=Path, default=Path("review/summary"))
    args = parser.parse_args()
    lit, stu = build(args.notes, args.out)
    print(f"wrote {args.out/'related-literature.md'} ({lit} works)")
    print(f"wrote {args.out/'related-studies.md'} ({stu} works)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
