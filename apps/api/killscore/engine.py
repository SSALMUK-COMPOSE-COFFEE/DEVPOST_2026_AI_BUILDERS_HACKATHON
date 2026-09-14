import ast
import copy
from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Mutant:
    id: str
    function: str
    operator: str
    line: int
    col: int
    description: str
    source: str


CMP_SWAP = {
    ast.Gt: (ast.GtE, ">", ">="),
    ast.GtE: (ast.Gt, ">=", ">"),
    ast.Lt: (ast.LtE, "<", "<="),
    ast.LtE: (ast.Lt, "<=", "<"),
    ast.Eq: (ast.NotEq, "==", "!="),
    ast.NotEq: (ast.Eq, "!=", "=="),
}

BOOL_SWAP = {
    ast.And: (ast.Or, "and", "or"),
    ast.Or: (ast.And, "or", "and"),
}


class _Site:
    def __init__(self, operator: str, node: ast.AST, description: str, apply):
        self.operator = operator
        self.node = node
        self.description = description
        self.apply = apply


def _sites(func: ast.FunctionDef) -> Iterator[_Site]:
    for node in ast.walk(func):
        if isinstance(node, ast.Compare):
            for i, op in enumerate(node.ops):
                if type(op) in CMP_SWAP:
                    new_cls, a, b = CMP_SWAP[type(op)]

                    def apply(n=node, i=i, new_cls=new_cls):
                        n.ops[i] = new_cls()

                    yield _Site("compare", node, f"{a} -> {b}", apply)
        elif isinstance(node, ast.BoolOp) and type(node.op) in BOOL_SWAP:
            new_cls, a, b = BOOL_SWAP[type(node.op)]

            def apply(n=node, new_cls=new_cls):
                n.op = new_cls()

            yield _Site("boolop", node, f"{a} -> {b}", apply)
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, bool):

                def apply(n=node):
                    n.value = not n.value

                yield _Site("bool_const", node, f"{node.value} -> {not node.value}", apply)
            elif isinstance(node.value, int) and not isinstance(node.value, bool):

                def apply(n=node):
                    n.value = n.value + 1

                yield _Site("int_const", node, f"{node.value} -> {node.value + 1}", apply)
        elif isinstance(node, ast.If):

            def apply(n=node):
                n.test = ast.UnaryOp(op=ast.Not(), operand=n.test)

            yield _Site("negate_if", node, "if cond -> if not cond", apply)
        elif isinstance(node, ast.Return) and node.value is not None and not isinstance(node.value, ast.Constant):

            def apply(n=node):
                n.value = ast.Constant(value=None)

            yield _Site("return_none", node, "return expr -> return None", apply)
        elif isinstance(node, ast.ExceptHandler):
            body = node.body
            if len(body) == 1 and isinstance(body[0], ast.Raise):

                def apply(n=node):
                    n.body = [ast.Pass()]

                yield _Site("swallow_except", node, "except: raise -> except: pass", apply)


def normalize(source: str) -> str:
    return ast.unparse(ast.parse(source))


def _functions(tree: ast.Module) -> list[ast.FunctionDef]:
    return [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]


def generate(source: str, only_functions: set[str] | None = None) -> list[Mutant]:
    tree = ast.parse(source)
    mutants: list[Mutant] = []
    for func_index, func in enumerate(_functions(tree)):
        if only_functions is not None and func.name not in only_functions:
            continue
        site_count = sum(1 for _ in _sites(func))
        for k in range(site_count):
            work = copy.deepcopy(tree)
            work_func = _functions(work)[func_index]
            site = list(_sites(work_func))[k]
            site.apply()
            ast.fix_missing_locations(work)
            mutants.append(
                Mutant(
                    id=f"{func.name}:{k}",
                    function=func.name,
                    operator=site.operator,
                    line=site.node.lineno,
                    col=site.node.col_offset,
                    description=site.description,
                    source=ast.unparse(work),
                )
            )
    return mutants
