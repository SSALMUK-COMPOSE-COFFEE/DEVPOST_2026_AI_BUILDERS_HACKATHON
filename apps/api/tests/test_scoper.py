from pathlib import Path

from killscore.scoper import as_filter, changed_lines, scope

SRC = '''def a():
    return 1


def b(x):
    if x > 1:
        return 2
    return 3


def c():
    return 4
'''

DIFF = '''diff --git a/mod.py b/mod.py
--- a/mod.py
+++ b/mod.py
@@ -5,3 +5,3 @@
 def b(x):
-    if x >= 1:
+    if x > 1:
         return 2
'''


def test_changed_lines_maps_new_side():
    assert changed_lines(DIFF) == {"mod.py": {6}}


def test_scope_picks_only_touched_function(tmp_path: Path):
    (tmp_path / "mod.py").write_text(SRC)
    targets = scope(tmp_path, DIFF)
    assert [(t.name, t.line_start, t.line_end) for t in targets] == [("b", 5, 8)]
    assert as_filter(targets) == {"mod.py": {"b"}}


def test_scope_ignores_missing_and_non_python(tmp_path: Path):
    diff = DIFF.replace("mod.py", "gone.py") + DIFF.replace("mod.py", "notes.md")
    assert scope(tmp_path, diff) == []
