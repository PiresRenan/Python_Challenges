from parser import Node, build_parse_tree


class Evaluator:
    def evaluate(self, root: Node) -> float:
        if root.value.isdigit() or (root.value.startswith("-") and root.value[1:].isdigit()):
            return float(root.value)
        elif root.value == "+":
            return self.evaluate(root.children[0]) + self.evaluate(root.children[1])
        elif root.value == "-":
            return self.evaluate(root.children[0]) - self.evaluate(root.children[1])
        elif root.value == "*":
            return self.evaluate(root.children[0]) * self.evaluate(root.children[1])
        elif root.value == "/":
            return self.evaluate(root.children[0]) / self.evaluate(root.children[1])
        else:
            raise ValueError("Operador inválido")


def evaluate_expression(expression: str) -> float:
    expression = expression.replace(" ", "")  # Remover espaços em branco
    root = build_parse_tree(expression)
    return Evaluator().evaluate(root)
