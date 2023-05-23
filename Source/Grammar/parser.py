import re
from Source.Grammar.lexer import *
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
            ast = self.assignment()
            print("Parsing completed successfully.")
            return ast
        except ValueError as e:
            print("Parsing error:", str(e))

    def match(self, token_type):
        if self.token_index < len(self.tokens):
            token = self.tokens[self.token_index]
            if token[0] == token_type:
                self.token_index += 1
                return token
            else:
                raise ValueError(f"Expected '{token_type}', but got '{token[0]}'")
        else:
            raise ValueError(f"Expected '{token_type}', but reached end of input")

    def assignment(self):
        identifier_token = self.match('Identifier')
        self.match('Operator')
        expression_ast = self.expression()
        self.match('Separator')
        return ('Assignment', identifier_token[1], expression_ast)

    def expression(self):
        term_ast = self.term()
        while self.token_index < len(self.tokens) and self.tokens[self.token_index][0] == 'Operator':
            operator_token = self.match('Operator')
            term_ast = ('Expression', term_ast, operator_token[1], self.term())
        return term_ast

    def term(self):
        factor_ast = self.factor()
        if self.token_index < len(self.tokens) and self.tokens[self.token_index][0] == 'Operator':
            operator_token = self.match('Operator')
            factor_ast = ('Term', factor_ast, operator_token[1], self.factor())
        return factor_ast

    def factor(self):
        if self.token_index < len(self.tokens):
            token = self.tokens[self.token_index]
            self.token_index += 1
            if token[0] in ('Identifier', 'Literal'):
                return token[1]
            elif token[0] == 'Lparen':
                expression_ast = self.expression()
                self.match('Rparen')
                return expression_ast
        raise ValueError("Invalid factor")

def build_ast(input_string):
    tokens = lexer(input_string)
    parser = Parser(tokens)
    return parser.parse()

