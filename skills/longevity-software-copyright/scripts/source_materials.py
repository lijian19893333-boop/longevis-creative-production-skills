#!/usr/bin/env python3
"""Inventory an explicit source list; select original lines with a provenance map.

This creates working text, not a filing-ready Word/PDF or a completeness opinion.
Only standard-library Python is needed. Run --help for both commands.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

CONTAINERS = {".mcp", ".mcgs", ".apk", ".aab", ".zip", ".rar", ".7z",
              ".exe", ".dll", ".so", ".bin", ".db", ".mdb"}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def physical_lines(text):
    """Split only file line endings, never Unicode characters inside a string."""
    if not text:
        return []
    lines = re.split(r"\r\n|\n|\r", text)
    if lines[-1] == "":
        lines.pop()
    return lines


def source_path(root, relative):
    path = Path(relative)
    if not relative or path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe relative path: {relative}")
    candidate = root / path
    if any(part.is_symlink() for part in [candidate, *candidate.parents] if part != root):
        raise ValueError(f"Symlinks are not supported: {relative}")
    if not candidate.is_file() or not candidate.resolve().is_relative_to(root):
        raise ValueError(f"Not a source file inside the root: {relative}")
    return candidate


def write_json_new(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def inventory(root, file_list, output, encoding="utf-8"):
    root = Path(root).resolve(strict=True)
    names = [line.strip() for line in Path(file_list).read_text(encoding="utf-8").splitlines()
             if line.strip()]
    if not names or len(names) != len(set(names)):
        raise ValueError("The file list must be nonempty with no duplicate paths")
    entries, seen = [], set()
    for name in names:
        path = source_path(root, name)
        if path in seen:
            raise ValueError(f"Duplicate source path: {name}")
        seen.add(path)
        data = path.read_bytes()
        entry = {"path": path.relative_to(root).as_posix(), "sha256": sha256(data),
                 "bytes": len(data)}
        if path.suffix.lower() in CONTAINERS or any(c < 32 and c not in (9, 10, 13) for c in data):
            entry.update(kind="native_or_binary", physical_lines=None, nonempty_lines=None)
        else:
            lines = physical_lines(data.decode(encoding, errors="strict"))
            entry.update(kind="text", physical_lines=len(lines),
                         nonempty_lines=sum(bool(line.strip()) for line in lines))
        entries.append(entry)
    result = {"format_version": 1, "encoding": encoding,
              "scope_status": "unreviewed", "scope_note": "Explicit file list only; completeness and ownership require human review.",
              "files": entries}
    write_json_new(output, result)
    return result


def extract(root, manifest, output_dir, name, version, lines_per_page=50, side_pages=30):
    root = Path(root).resolve(strict=True)
    output_dir = Path(output_dir).resolve()
    if output_dir.exists():
        raise FileExistsError(f"Output already exists: {output_dir}")
    if output_dir.is_relative_to(root):
        raise ValueError("Put generated materials outside the source root")
    if not name.strip() or not version.strip() or lines_per_page < 1 or side_pages < 1:
        raise ValueError("Provide name, version and positive pagination settings")
    data = json.loads(Path(manifest).read_text(encoding="utf-8"))
    if data.get("format_version") != 1 or not data.get("files"):
        raise ValueError("Unsupported or empty manifest")
    rows, paths = [], set()
    for entry in data["files"]:
        relative = entry["path"]
        path = source_path(root, relative)
        if path in paths:
            raise ValueError(f"Duplicate source in manifest: {relative}")
        paths.add(path)
        raw = path.read_bytes()
        if sha256(raw) != entry["sha256"]:
            raise ValueError(f"Source changed since inventory: {relative}")
        if entry["kind"] != "text":
            raise ValueError(f"Native/binary project requires a platform export before text extraction: {relative}")
        for number, line in enumerate(physical_lines(raw.decode(data["encoding"], errors="strict")), 1):
            if line.strip():
                rows.append({"path": relative, "line": number, "global_line": len(rows) + 1,
                             "text": line})
    if not rows:
        raise ValueError("No nonempty source lines; do not pad or invent code")
    side = side_pages * lines_per_page
    mode = "all" if len(rows) <= side * 2 else "front-back"
    selected = rows if mode == "all" else rows[:side] + rows[-side:]
    text = "\n".join(row["text"] for row in selected) + "\n"
    pages = []
    for start in range(0, len(selected), lines_per_page):
        block = selected[start:start + lines_per_page]
        pages.append({"number": len(pages) + 1,
                      "segment": "all" if mode == "all" else ("front" if start < side else "back"),
                      "rows": [{key: value for key, value in row.items() if key != "text"} for row in block]})
    report = {"software_name": name, "version": version, "mode": mode,
              "source_files": len(paths), "total_nonempty_lines": len(rows),
              "selected_lines": len(selected), "logical_pages": len(pages),
              "lines_per_page": lines_per_page, "side_pages": side_pages,
              "selected_text_sha256": sha256(text.encode("utf-8")),
              "scope_status": "unreviewed",
              "verification": "Selected files match inventory hashes. Scope, rights, rendering and filing readiness remain unreviewed.",
              "layout_note": "Blank-only lines omitted; CRLF/CR line endings normalized to LF. All other retained characters and original physical line numbers preserved. Comments retained."}
    output_dir.mkdir(parents=True)
    (output_dir / "selected-source.txt").write_text(text, encoding="utf-8")
    write_json_new(output_dir / "pages.json", {"software_name": name, "version": version, "pages": pages})
    write_json_new(output_dir / "source-manifest.json", data)
    write_json_new(output_dir / "review.json", report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    inv = commands.add_parser("inventory", help="Hash an explicitly ordered UTF-8 list of relative paths")
    inv.add_argument("root", type=Path)
    inv.add_argument("--files", required=True, type=Path)
    inv.add_argument("--out", required=True, type=Path)
    inv.add_argument("--encoding", default="utf-8")
    ext = commands.add_parser("extract", help="Select all or first/last source lines; preserve provenance")
    ext.add_argument("root", type=Path)
    ext.add_argument("--manifest", required=True, type=Path)
    ext.add_argument("--out-dir", required=True, type=Path)
    ext.add_argument("--name", required=True)
    ext.add_argument("--version", required=True)
    ext.add_argument("--lines-per-page", type=int, default=50)
    ext.add_argument("--side-pages", type=int, default=30)
    args = parser.parse_args()
    try:
        if args.command == "inventory":
            result = inventory(args.root, args.files, args.out, args.encoding)
            summary = {"files": len(result["files"]), "scope_status": result["scope_status"]}
        else:
            summary = extract(args.root, args.manifest, args.out_dir, args.name,
                              args.version, args.lines_per_page, args.side_pages)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError, LookupError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
