#!/usr/bin/env python3
"""Flag LaTeX in Markdown that GitHub's Markdown pass breaks before the math renderer sees it.

Usage: python3 check_github_math.py FILE.md [FILE.md ...]

Offline and heuristic. It reports `file:line: [code] message`, and exits 1 if anything was found.
It cannot see GitHub's macro filter beyond the short list in BLOCKED, and it does not replace a look
at the rendered page.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PUNCT = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
# Blocked by GitHub's macro filter: \operatorname observed, the others reported by other users.
BLOCKED = ("operatorname", "phantom", "newcommand", "renewcommand", "def")
BLOCK_START = re.compile(r"^ {0,3}([-+*](\s|$)|#{1,6}(\s|$)|>|\d{1,9}[.)](\s|$))")
ESCAPES = {
    ",": "\\thinspace", ";": "\\thickspace", ":": "\\medspace", "!": "\\negthinspace",
    "{": "\\lbrace", "}": "\\rbrace", "|": "\\Vert", "_": "a letter-only name",
    "%": "\\text{\\%} in protected math", "&": "protected math", "#": "protected math",
    "$": "protected math",
}


def blank_code(line: str) -> str:
    """Replace inline code spans (including $`...`$ math) by spaces, keeping columns."""
    return re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), line)


def can_open(text: str, i: int) -> bool:
    prev, nxt = (text[i - 1] if i else " "), (text[i + 1] if i + 1 < len(text) else " ")
    left = not nxt.isspace() and (nxt not in PUNCT or prev.isspace() or prev in PUNCT)
    right = not prev.isspace() and (prev not in PUNCT or nxt.isspace() or nxt in PUNCT)
    return left if text[i] == "*" else left and (not right or prev in PUNCT)


def can_close(text: str, i: int) -> bool:
    prev, nxt = (text[i - 1] if i else " "), (text[i + 1] if i + 1 < len(text) else " ")
    left = not nxt.isspace() and (nxt not in PUNCT or prev.isspace() or prev in PUNCT)
    right = not prev.isspace() and (prev not in PUNCT or nxt.isspace() or nxt in PUNCT)
    return right if text[i] == "*" else right and (not left or nxt in PUNCT)


def check(path: Path) -> list[str]:
    out: list[str] = []

    def report(n: int, code: str, message: str) -> None:
        out.append(f"{path}:{n}: [{code}] {message}")

    lines = path.read_text(encoding="utf-8").split("\n")
    fence: tuple[str, bool] | None = None  # (marker, is a ```math fence) while a code fence is open
    display = False  # inside a multi-line $$ block
    paragraph: list[tuple[int, str, bool]] = []  # (line number, text, is display math)

    def flush() -> None:
        """Emphasis pairs form within one paragraph, across formulas and lines."""
        chars = [(n, col, ch, text, disp) for n, text, disp in paragraph for col, ch in enumerate(text)]
        spans = {}
        for n, text, disp in paragraph:
            inline = [m.span() for m in re.finditer(r"\$[^$]+\$", text)]
            spans[n] = (disp, inline)

        def in_math(n: int, col: int) -> bool:
            disp, inline = spans[n]
            return disp or any(a <= col < b for a, b in inline)

        for mark in "_*":
            opener = None
            for n, col, ch, text, _ in chars:
                if ch != mark or text[col : col + 2] == "**" or (col and text[col - 1] == "*" and mark == "*"):
                    continue
                if opener and can_close(text, col) and (in_math(n, col) or in_math(*opener)):
                    fix = "write ^\\ast" if mark == "*" else "put a letter before it (\\bar X_i, \\rbrack_i)"
                    report(opener[0], "emphasis", f"'{mark}' here pairs with the '{mark}' on line {n} "
                           f"as Markdown emphasis; {fix}, or use protected math")
                    opener = None
                elif can_open(text, col) and in_math(n, col):
                    opener = (n, col)
        paragraph.clear()

    for n, raw in enumerate(lines, 1):
        stripped = raw.strip()
        marker = re.match(r"^ {0,3}(```+|~~~+)(.*)$", raw)
        if fence:
            if marker and marker.group(1).startswith(fence[0]) and not marker.group(2).strip():
                fence = None
            elif fence[1]:
                for name in BLOCKED:
                    if re.search(rf"\\{name}\b", raw):
                        report(n, "macro", f"\\{name} is blocked by GitHub's macro filter")
            continue
        if marker:
            flush()
            fence = (marker.group(1), marker.group(2).strip() == "math")
            continue

        prose_code_blanked = re.sub(r"(?<!\$)`[^`]*`", "", raw)  # keep $`...`$ math, drop other code spans
        for name in BLOCKED:
            if re.search(rf"\\{name}\b", prose_code_blanked):
                report(n, "macro", f"\\{name} is blocked by GitHub's macro filter"
                       + ("; use \\mathop{\\mathrm{...}}" if name == "operatorname" else ""))

        if stripped == "$$":
            if not display:
                flush()
                if n > 1 and lines[n - 2].strip():
                    report(n, "block", "$$ must follow a blank line, or it is not read as display math")
                if raw.startswith("  ") and any(re.match(r"^\s*([-+*]|\d+[.)])\s", p) for p in lines[max(0, n - 12) : n - 1]):
                    report(n, "block", "$$ inside a list item is not rendered; use a ```math fence there")
            else:
                flush()
                if n < len(lines) and lines[n].strip():
                    report(n, "block", "$$ must be followed by a blank line, or the block is not rendered")
            display = not display
            continue

        text = blank_code(raw)
        if display:
            if not stripped:
                report(n, "block", "blank line inside $$ splits the block")
            if BLOCK_START.match(raw):
                report(n, "block", "math line starts like a Markdown list, heading or quote; "
                       "move the leading sign to the end of the previous line")
            math_parts = [(0, text)]
        else:
            if not stripped:
                flush()
                continue
            math_parts = [(m.start(), m.group(0)) for m in re.finditer(r"\$\$?[^$]+\$\$?", text)]
            for m in re.finditer(r"(?<!\$)\$(?!\$)([^$]+)\$(?!\$)", text):
                inner = m.group(1)
                if inner != inner.strip() or not inner.strip():
                    continue  # not read as math (currency), or protected $`...`$ math
                before = text[m.start() - 1] if m.start() else " "
                after = text[m.end()] if m.end() < len(text) else " "
                if not (before.isspace() or before in "(*"):
                    report(n, "delimiter", f"'{before}' directly before the opening $ of ${inner[:20]}$ "
                           "stops it being read as math; put a space there")
                elif after.isalnum() or after in "]'\"" or (inner[-1] in PUNCT and after in ")]"):
                    report(n, "delimiter", f"'{after}' directly after the closing $ of ${inner[:20]}$ "
                           "stops it being read as math; put a space there")
            if re.search(r"\\\(|\\\)|^\s*\\\[\s*$", text):
                report(n, "delimiter", "\\( \\) and \\[ \\] are not math delimiters on GitHub; use $ and $$")
        paragraph.append((n, text, display))

        for _, part in math_parts:
            for m in re.finditer(r"\\([^A-Za-z\s])", part):
                ch = m.group(1)
                if ch == "\\":
                    if display and part[m.end():].strip() == "":
                        continue
                    report(n, "escape", "'\\\\' survives only at the end of a line inside a multi-line $$ "
                           "block; break the line after it, or use a ```math fence")
                elif ch in ESCAPES:
                    report(n, "escape", f"'\\{ch}' loses its backslash on GitHub; use {ESCAPES[ch]}")
            if re.search(r"<[A-Za-z/][^>]*>", part):
                report(n, "html", "'<...>' is read as an HTML tag and stops math for the rest of the "
                       "page; use \\lt and \\gt")
            if "](" in part:
                report(n, "link", "'[...](...)' is read as a Markdown link; use \\lbrack \\rbrack")
            if part.count("~") >= 2:
                report(n, "strike", "two '~' are read as strikethrough; use \\ (backslash space) or \\nobreakspace")
            if stripped.startswith("|") and "|" in part.strip("$"):
                report(n, "table", "'|' inside math splits a table cell; use \\vert or \\Vert")
    flush()
    return sorted(set(out), key=lambda item: int(item.split(":")[1]))


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    findings = [line for name in sys.argv[1:] for line in check(Path(name))]
    print("\n".join(findings) if findings else "No GitHub math hazards found.")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
