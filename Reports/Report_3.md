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

first we need to identifiy the keywords which the lexer will recognize as keywords
```
symbols = ['{', '}', '(', ')', '[', ']', '.', '*', ':', ',', '=', '+', '-', ';'] # single-char keywords
    punctiuation = ["'", '"']
    long_comment = ['/*', '*/'] # multi-char keywords
    short_comment = ['#','//']
    keywords = ['public', 'main','static', 'void','for','System', 'out', 'print']
    oprerators = ['String', 'int', 'double', 'float', 'bool', 'list', 'class']
    KEYWORDS = symbols + long_comment + keywords + short_comment + oprerators
```

now we need to break down the given script into it's smallest elements:(words,symbols,newlines) and here's the loop that goes through each character in the code and devides it:
```
    for i,char in enumerate(string):
        if char == '*':
            if string[i-1] == '/':
                lexeme += '/*'
            elif string[i+1] == '/':
                lexeme += '*/'
            else:
                lexeme += '*'
        elif char == '/':
            if string[i+1] != '*' and string[i-1] != '*':
                lexeme += '/'
            else:
                continue
        elif char == '\n':
            lexems.append(lexeme)
            lexeme = ''
        else:
            if char != white_space:
                lexeme += char # adding a char each time
        if (i+1 < len(string)): # prevents error
            if string[i+1] == white_space or string[i+1] in KEYWORDS or lexeme in KEYWORDS: # if next char == ' '
                if lexeme != '':
```
which we take and add to a list called lexems
```
lexems.append(lexeme)
lexeme = ''
```
then we need to compare every lexeme to the list's of the keyword and classify them accordingly
*this is a part of the whole script
```
 for string in lexems:
        if string in long_comment:
            print(f"token: comment_Operator Value: {string}")
            longComment = not longComment
        if string in short_comment:
            print(f"token: comment_Operator Value: {string}")
            isComment = True
        if (isComment == True) and (string == '\n') or (string == '!'):
            print(f"token: comment Value= !")
            print(f"token: <newLine>")
            isComment = False
        if isOperator == True and string not in symbols:
            print(f"token: Definer Value: {string}")
            isOperator = False
            definers.append(string)
        elif longComment == True or isComment == True:
            print(f"token: comment Value: {string}")
        elif string == '\n':
            print(f"token: <newline>")
        elif string in symbols:
```


## Conclusions / Screenshots / Results

In this laboratory work I learned and implemented the lexer for simple mathematical calculations.
I understood what lexical analysis is and got familiar with the inner workings of a tokenizer

## Results:

For the inputted string:  "int d = (b * b) - 4( a * c)" I got the following output:
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
