from typing import List
from lexer import Token, Lexer


class Node:
    def __init__(self, value: str):
        self.value = value
        self.children = []

    def add_child(self, child: 'Node'):
        self.children.append(child)


class Parser:
    def __init__(self, expression: str):
        self.tokens = Lexer(expression).tokenize()
        self.current_token = None
        self.pos = 0

    def parse(self) -> Node:
        self._advance()
        return self._parse_expression()

    def _advance(self):
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
            self.pos += 1
        else:
            self.current_token = Token("EOF", "")

    def _parse_expression(self) -> Node:
        node = self._parse_term()

        while self.current_token.type in ("+", "-"):
            operator = self.current_token
            self._advance()
            right = self._parse_term()
            node = Node(operator.value)
            node.add_child(node)
            node.add_child(right)

        return node

    def _parse_term(self) -> Node:
        node = self._parse_factor()

        while self.current_token.type in ("*", "/"):
            operator = self.current_token
            self._advance()
            right = self._parse_factor()
            node = Node(operator.value)
            node.add_child(node)
            node.add_child(right)

        return node

    def _parse_factor(self) -> Node:
        token = self.current_token
        self._advance()

        if token.type == "NUMBER":
            return Node(token.value)
        elif token.type == "OPERATOR" and token.value == "-":
            node = Node("-")
            node.add_child(Node("0"))
            node.add_child(self._parse_factor())
            return node
        elif token.type == "OPERATOR" and token.value == "+":
            return self._parse_factor()
        else:
            raise ValueError("Expressão inválida")


def build_parse_tree(expression: str) -> Node:
    parser = Parser(expression)
    return parser.parse()
