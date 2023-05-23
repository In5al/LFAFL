
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

def lexer(input_string):
    tokens = []
    while input_string:
        match = None
        for token_type, regex_pattern in TOKEN:
            regex = re.compile(regex_pattern)
            match = regex.match(input_string)
            if match:
                tokens.append((token_type, match.group(0)))
                input_string = input_string[match.end():].lstrip()
                break
        if not match:
            raise ValueError(f"Invalid input at position {len(input_string)}: {input_string}")
    return tokens
#
