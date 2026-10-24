#!/usr/bin/env python3
"""
Puts a figure on the bench: `python build.py <figure.js> [out.html]` writes
one self-contained page, bench.html with kernel.js and the figure in its two
slots and nothing else changed, and prints where it is. Without a path the
page is hairline-<name>.html in the working directory.
"""
import sys
import re
from pathlib import Path

here = Path(__file__).resolve().parent

def assemble(figure: str) -> str:
    kernel = (here / "kernel.js").read_text(encoding="utf-8").replace("\r\n", "\n").rstrip()
    bench = (here / "bench.html").read_text(encoding="utf-8").replace("\r\n", "\n")
    clean_figure = figure.replace("\r\n", "\n").strip()
    return bench.replace("/*KERNEL*/", f"\n{kernel}\n").replace("/*FIGURE*/", f"\n{clean_figure}\n")

def name_of(figure: str):
    matches = list(re.finditer(r"\bhairline\s*\(\s*\{", figure))
    if not matches:
        return None
    last_call = matches[-1]
    name_match = re.search(r'\bname:\s*["\'`]([a-z][a-z0-9-]*)["\'`]', figure[last_call.start():])
    return name_match.group(1) if name_match else None

def main():
    if len(sys.argv) < 2:
        print("usage: python build.py <figure.js> [out.html]", file=sys.stderr)
        sys.exit(2)
    src_path = Path(sys.argv[1])
    figure_code = src_path.read_text(encoding="utf-8")
    fig_name = name_of(figure_code) or "figure"
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(f"hairline-{fig_name}.html")
    out_path.write_text(assemble(figure_code), encoding="utf-8")
    print(out_path.resolve())

if __name__ == "__main__":
    main()
