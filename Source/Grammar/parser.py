import re

# Define regular expressions for different types of tokens
TOKEN = [
    ('Identifier', r'[a-zA-Z]\w*'),
    ('Literal', r'\d+'),
    ('Operator', r'[+\-*\/=]'),
    ('Separator', r';'),
    ('Lparen', r'\('),
    ('Rparen', r'\)')
]

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def parse(self):
        try:
            self.assignment()
            print("Parsing completed successfully.")
        except ValueError as e:
            print("Parsing error:", str(e))

    def match(self, token_type):
        if self.token_index < len(self.tokens):
            token = self.tokens[self.token_index]
            if token[0] == token_type:
                self.token_index += 1
            else:
                raise ValueError(f"Expected '{token_type}', but got '{token[0]}'")
        else:
            raise ValueError(f"Expected '{token_type}', but reached end of input")

    def assignment(self):
        self.match('Identifier')
        self.match('Operator')
        self.expression()
        self.match('Separator')

    def expression(self):
        self.term()
        while self.token_index < len(self.tokens) and self.tokens[self.token_index][0] == 'Operator':
            self.match('Operator')
            self.term()

    def term(self):
        self.factor()
        if self.token_index < len(self.tokens):
            if self.tokens[self.token_index][0] == 'Operator':
                self.match('Operator')
                self.factor()

    def factor(self):
        if self.token_index < len(self.tokens):
            if self.tokens[self.token_index][0] == 'Identifier':
                self.match('Identifier')
            elif self.tokens[self.token_index][0] == 'Literal':
                self.match('Literal')
            elif self.tokens[self.token_index][0] == 'Lparen':
                self.match('Lparen')
                self.expression()
                self.match('Rparen')
            else:
                raise ValueError("Invalid factor")


