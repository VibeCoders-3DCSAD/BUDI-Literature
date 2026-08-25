#!/usr/bin/env python3
import os, sys, hashlib, argparse
from collections import defaultdict
from PyPDF2 import PdfReader
import difflib

VISUAL_AVAILABLE = False
try:
    import fitz
    from PIL import Image
    import imagehash
    VISUAL_AVAILABLE = True
except ImportError:
    pass

_text_cache = {}

def extract_text(filepath):
    if filepath in _text_cache:
        return _text_cache[filepath]
    try:
        reader = PdfReader(filepath)
        text_parts = []
        for page in reader.pages:
            txt = page.extract_text()
            if txt:
                text_parts.append(txt)
        full = "".join(text_parts)
        _text_cache[filepath] = full
        return full
    except Exception:
        _text_cache[filepath] = ""
        return ""

def byte_hash(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def content_hash(filepath):
    text = extract_text(filepath)
    if not text.strip():
        return byte_hash(filepath)
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def visual_hash(filepath):
    if not VISUAL_AVAILABLE:
        return None
    try:
        doc = fitz.open(filepath)
        if doc.page_count == 0:
            doc.close()
            return None
        page = doc[0]
        pix = page.get_pixmap(dpi=150)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        doc.close()
        return imagehash.average_hash(img)
    except Exception:
        return None

def are_textually_similar(fp1, fp2, threshold=0.95):
    t1 = extract_text(fp1)
    t2 = extract_text(fp2)
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return difflib.SequenceMatcher(None, t1, t2).ratio() >= threshold

def are_visually_similar(fp1, fp2, threshold=0.9):
    h1 = visual_hash(fp1)
    h2 = visual_hash(fp2)
    if h1 is None or h2 is None:
        return False
    max_dist = int(len(h1.hash) ** 2 * (1 - threshold))
    return (h1 - h2) <= max_dist

def are_duplicates_cascade(fp1, fp2, sim_threshold=0.95, vis_threshold=0.9):
    # 1. text similarity
    if not are_textually_similar(fp1, fp2, sim_threshold):
        return False
    # 2. content hash
    if content_hash(fp1) != content_hash(fp2):
        return False
    # 3. byte hash – if this matches, we're done (100% identical)
    if byte_hash(fp1) == byte_hash(fp2):
        return True
    # 4. visual (only if byte hash differs, i.e., scanned but visually same)
    if VISUAL_AVAILABLE:
        if are_visually_similar(fp1, fp2, vis_threshold):
            return True
    return False

def find_duplicates(directories, method=None, cascade=False,
                    sim_threshold=0.95, vis_threshold=0.9):
    pdf_files = []
    for d in directories:
        if not os.path.isdir(d):
            print(f"Warning: {d} not a directory", file=sys.stderr)
            continue
        for root, _, files in os.walk(d):
            for f in files:
                if f.lower().endswith('.pdf'):
                    pdf_files.append(os.path.join(root, f))
    if len(pdf_files) < 2:
        print("Need at least two PDFs.", file=sys.stderr)
        return {}

    print(f"Found {len(pdf_files)} PDF files.", file=sys.stderr)

    if not cascade and method:
        groups = defaultdict(list)
        print(f"Using method: {method}", file=sys.stderr)
        for i, fp in enumerate(pdf_files):
            if i % 50 == 0:
                print(f"  Hashing {i}/{len(pdf_files)}...", file=sys.stderr)
            if method == 'byte':
                sig = byte_hash(fp)
            elif method == 'text_hash':
                sig = content_hash(fp)
            elif method == 'visual':
                sig = visual_hash(fp)
                if sig is None:
                    sig = f"none_{fp}"
            else:
                raise ValueError(f"Unknown method: {method}")
            groups[sig].append(fp)
        # print groups with size > 1
        return {k: v for k, v in groups.items() if len(v) > 1}

    elif cascade:
        print("Running cascade (text → content hash → byte hash → visual)", file=sys.stderr)
        visited = set()
        groups = []
        total = len(pdf_files)
        for i in range(total):
            if i % 50 == 0:
                print(f"  Comparing {i}/{total}...", file=sys.stderr)
            if pdf_files[i] in visited:
                continue
            group = [pdf_files[i]]
            for j in range(i+1, total):
                if pdf_files[j] in visited:
                    continue
                if are_duplicates_cascade(pdf_files[i], pdf_files[j],
                                          sim_threshold, vis_threshold):
                    group.append(pdf_files[j])
                    visited.add(pdf_files[j])
            if len(group) > 1:
                groups.append(group)
            visited.add(pdf_files[i])
        result = {}
        for idx, g in enumerate(groups):
            result[f"group_{idx+1}"] = g
        return result
    else:
        print("Specify --method or --cascade", file=sys.stderr)
        return {}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directories', nargs='+')
    parser.add_argument('--method', choices=['byte','text_hash','visual','text_sim'])
    parser.add_argument('--cascade', action='store_true')
    parser.add_argument('--sim-threshold', type=float, default=0.95)
    parser.add_argument('--vis-threshold', type=float, default=0.9)
    args = parser.parse_args()
    if not args.cascade and not args.method:
        print("Error: need --method or --cascade", file=sys.stderr)
        sys.exit(1)
    _text_cache.clear()
    dupes = find_duplicates(args.directories, args.method, args.cascade,
                            args.sim_threshold, args.vis_threshold)
    if not dupes:
        print("No duplicates found.")
    else:
        print(f"\nFound {len(dupes)} duplicate groups:")
        for key, files in dupes.items():
            print(f"  {key}:")
            for f in files:
                print(f"    {f}")

if __name__ == "__main__":
    main()