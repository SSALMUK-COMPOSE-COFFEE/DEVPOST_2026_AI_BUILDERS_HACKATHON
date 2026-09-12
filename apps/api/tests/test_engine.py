import ast

from killscore.engine import generate

SRC = '''
def gate(score, threshold):
    if score > threshold and threshold > 0:
        return True
    return False

def safe(x):
    try:
        return x + 1
    except Exception:
        raise
'''


def test_generates_mutants_for_each_site():
    mutants = generate(SRC)
    ops = {m.operator for m in mutants}
    assert {"compare", "boolop", "bool_const", "int_const", "negate_if", "return_none", "swallow_except"} <= ops


def test_each_mutant_parses_and_differs():
    original = ast.unparse(ast.parse(SRC))
    for m in generate(SRC):
        ast.parse(m.source)
        assert m.source != original


def test_only_functions_filter():
    mutants = generate(SRC, only_functions={"safe"})
    assert {m.function for m in mutants} == {"safe"}


def test_compare_flip_description():
    m = next(m for m in generate(SRC) if m.operator == "compare")
    assert m.description == "> -> >="
    assert ">=" in m.source
