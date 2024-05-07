from typing import List
from dataclasses import dataclass


@dataclass
class Token:
    type: str
    value: str


class Lexer:
    def __init__(self, expression: str):
        self.expression = expression
        self.pos = 0

    def get_next_token(self) -> Token:
        while self.pos < len(self.expression) and self.expression[self.pos] == " ":
            self.pos += 1

        if self.pos >= len(self.expression):
            return Token("EOF", "")

        current_char = self.expression[self.pos]

        if current_char.isdigit():
            return self._get_number_token()
        elif current_char in "+-*/":
            self.pos += 1
            return Token("OPERATOR", current_char)
        else:
            raise ValueError(f"Caractere inválido: {current_char}")

    def _get_number_token(self) -> Token:
        start_pos = self.pos
        while (self.pos < len(self.expression) and
               self.expression[self.pos].isdigit()):
            self.pos += 1
        return Token("NUMBER", self.expression[start_pos:self.pos])

    def tokenize(self) -> List[Token]:
        tokens = []
        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == "EOF":
                break
        return tokens
