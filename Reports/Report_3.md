# Lexer & Scanner

## University: Technical University of Moldova

## Course: Formal Languages & Finite Automata

### Author: Carp Dan-Octavian
----

## Theory
A lexer is a component of the compiler that takes a stream of characters as input, then it  breaks down each line of code and outputs a sequence of tokens that define and operate in a given programming language

The task of the lexer is to identify and group together the characters of the input stream that form individual tokens, such as keywords, identifiers, operators, and literals

****Tokens**** within parsers correspond to ****terminal symbols**** within formal grammars.


## Objectives:

* Understand what lexical analysis [1] is.
* Get familiar with the inner workings of a lexer/scanner/tokenizer.
* Implement a sample lexer and show how it works.


## Implementation description

I wrote a lexer for basic programming language expressions. Its job is to take an input string and split it into smaller parts called tokens. Each token represents a different part of the expression. B. Names, Numbers, Symbols, Parentheses. These tokens can be used by parsers to understand and interpret expressions. 
```
import re
```
First we begin by importing the built-in module called "re". This module gives us the libert to work with regular expresions.By importing "re," you can perform tasks like pattern matching, string searching, string replacement, and string splitting in your program.
```
TOKEN = [
    ('Identifier', r'[a-zA-Z]\w*'),
    ('Literal', r'\d+'),
    ('Operator', r'[+\-*\/=]'),
    ('Separator', r';'),
    ('Lparen', r'\('),
    ('Rparen', r'\)')
]
```
We follow by created a list of tuples that define regular exporesions for different languages.Each of the defined token represents a specific element like identifiers, literals, operators,separators and parantheses.Regular expresions are used to math and identify wirh input string
```
    def lexer(input_string):
    tokens = []
```
We then create a function `lexer` that will take as input `input_string`. The purpose of this function is to toxenize the `input_string`, by that we understand breaking it down into smaller units called tokens which can represent distinct elements, things like identifiers, operators, separators, parantheses. Additioanlly, inside the function an empty list called `tokens` is initialized.The list will have this identified tokens as the function processes the `input_string`.
```
    while input_string:
        match = None
        for token_type, regex_pattern in TOKEN:
            regex = re.compile(regex_pattern)
            match = regex.match(input_string)
 ```
 By this part of the code we we have a `while` loop that iterates as long as there is content in our `input_string`. Within a loop, for the `match` variable the value is atributed to `None`. Next, with `for` we enter in a loop that iterates over the `TOKEN` list, which contains token types and their regular expression patterns. For each token type and regex pattern pair, a regular expression object is created using `re.copile()` and stored in `regex` variable.Finally the `match` variable is updated as it tries to match `regex` patern against the `input_strirng` using `regex.match(input_string)`. This verifies if the beginning of the `input_string` matches the pattern specifies by the regular expression
 ```
            if match:
                tokens.append((token_type, match.group(0)))
                input_string = input_string[match.end():].lstrip()
                break
```
Here we have an `if` statement that checks if a match was found using the regular expression pattern. If a match is found, it appends the matched token  to the `tokens` list and updated the `input_string`. The matched portion is removed usinf slicing `input_string[match.end():]` and removes leading whitespace using `lstrip()`. The `break` is used to exit the inner `for` as the match has been found and processed.
````
        if not match:
            raise ValueError(f"Invalid input at position {len(input_string)}: {input_string}")
    return tokens
````
Lastly we have an `if` statement that checks of no match was found using any of the regular expression patterns.If there is no match, it raises a `ValueError` with a specifiv error message which tells that the input position is invalid and so is the content of the input string at that possition.And at the end,the function returns the `tokens` list, which contains the identified tokens from the input string.



## Conclusions / Screenshots / Results

In this laboratory work I developed an initial implementation of a lexer in a programming language.The lexer takes an input string and breaks it down into tokens based on predefined patterns
The code can be futher improved by adding whitespace as well as error handling howeverr in my few attemps and limited time I encoutered a blockage and was unable to solve it.
## Results:

For the inputted string:  "int d = (b * b) - 4( a * c);" I got the following output:
```
----------------------------------------------------------------------------------
('Identifier', 'd')
('Operator', '=')
('Lparen', '(')
('Identifier', 'b')
('Operator', '*')
('Identifier', 'b')
('Rparen', ')')
('Operator', '-')
('Literal', '4')
('Lparen', '(')
('Identifier', 'a')
('Operator', '*')
('Identifier', 'c')
('Rparen', ')')
('Separator', ';')
---------------------------------------------------------------------------------
```
## References
[1] [Lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
