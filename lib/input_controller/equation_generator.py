import random
import math
import ast
import operator
# from configs.gameconf import GAME_DIFFICULTY
# simple math problem generator
# will generate an equations and return a tuple(equation, answer)

OPER_LIST = ["+", "-"]
OP_MAP = {
    ast.Add: operator.add,
    ast.Sub: operator.sub
}


def tree_node(left, right, oper):
    # string = f"{left} {oper} {right}"
    # return string
    case = random.randint(0, 1)
    if case:
        string = f"{left} {oper} {right}"
        return string
    string = f"({left} {oper} {right})"
    return string


def build_tree(num_nodes):
    if num_nodes == 1:
        return random.randrange(1, 10)

    num_left = math.floor(num_nodes / 2)
    left_subtree = build_tree(num_left)
    num_right = math.ceil(num_nodes / 2)
    right_subtree = build_tree(num_right)

    r_index = random.randrange(0, len(OPER_LIST))
    opr = OPER_LIST[r_index]
    return tree_node(left_subtree, right_subtree, opr)


class Calc(ast.NodeVisitor):

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return OP_MAP[type(node.op)](left, right)

    def visit_Num(self, node):
        return node.n

    def visit_Expr(self, node):
        return self.visit(node.value)

    @classmethod
    def evaluate(cls, expression):
        tree = ast.parse(expression)
        calc = cls()
        return calc.visit(tree.body[0])


def get_number_of_nodes():
    start = 2
    stop = 4
    num_nodes = random.randint(start, stop)
    return num_nodes


def generate_equation():
    problem = build_tree(get_number_of_nodes())
    answer = Calc.evaluate(problem)
    return problem, answer
