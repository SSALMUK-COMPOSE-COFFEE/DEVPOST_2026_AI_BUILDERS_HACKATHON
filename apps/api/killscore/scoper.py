import ast
import re
from dataclasses import dataclass
from pathlib import Path

HUNK = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")
FILE = re.compile(r"^\+\+\+ (?:b/)?(.+)$")


@dataclass(frozen=True)
class Target:
    file: str
    name: str
    line_start: int
    line_end: int


def changed_lines(diff: str) -> dict[str, set[int]]:
    out: dict[str, set[int]] = {}
    current: str | None = None
    new_line = 0
    for raw in diff.splitlines():
        m = FILE.match(raw)
        if m:
            current = m.group(1).strip()
            if current == "/dev/null":
                current = None
            else:
                out.setdefault(current, set())
            continue
        if raw.startswith("--- "):
            continue
        h = HUNK.match(raw)
        if h:
            new_line = int(h.group(1))
            continue
        if current is None:
            continue
        if raw.startswith("+"):
            out[current].add(new_line)
            new_line += 1
        elif raw.startswith("-"):
            out[current].add(new_line)
        elif raw.startswith("\\"):
            continue
        else:
            new_line += 1
    return out


def functions_touching(source: str, lines: set[int]) -> list[tuple[str, int, int]]:
    tree = ast.parse(source)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            start, end = node.lineno, node.end_lineno or node.lineno
            if any(start <= ln <= end for ln in lines):
                hits.append((node.name, start, end))
    return hits


def scope(repo: Path, diff: str) -> list[Target]:
    targets: list[Target] = []
    for file, lines in changed_lines(diff).items():
        if not file.endswith(".py"):
            continue
        path = repo / file
        if not path.exists():
            continue
        for name, start, end in functions_touching(path.read_text(), lines):
            targets.append(Target(file, name, start, end))
    return targets


def as_filter(targets: list[Target]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for t in targets:
        out.setdefault(t.file, set()).add(t.name)
    return out
