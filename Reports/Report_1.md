# Intro to formal languages. Regular grammars. Finite Automata.
## University: Technical University of Moldova
## Course: Formal Languages & Finite Automata
### Author: Carp Dan-Octavian

----

## Theory
A formal language is a set of finite-length sequences of symbols that are constructed according to a set of well-defined rules or grammar. These sequences are often called strings, and the symbols used to construct the strings are drawn from a finite set of characters, called the alphabet.

Formal languages are used to describe various types of languages, including programming languages, regular languages, context-free languages, and others. The rules that govern formal languages are usually defined using a set of production rules, which specify how the symbols in the language can be combined to form valid strings.

In the context of formal languages and finite state machines, a grammar refers to a set of rules for constructing sequences of strings or symbols that are valid in a formal language. These rules define how language symbols are combined to form valid strings associated with the language.

Grammar is often described using production rules that specify how symbols are replaced or combined to form new symbols or strings. For example, a production rule may stipulate that symbol A can be replaced by a series of symbols "BCD", or symbol B can be replaced by symbol "a".

There are several types of grammars commonly used in formal language theory, including regular grammars, context-free grammars, and context-sensitive grammars. The type of grammar used to describe a particular formal language depends on the complexity of the language and the types of strings the language can produce.

Grammar plays an important role in the study of formal languages and finite automata because it provides a way to formally describe and analyze the structure and behavior of languages. By defining the rules for constructing strings that are valid in the language, grammars allow us to think about the properties of the language and the algorithms and systems that process linguistic input. 

A finite state machine is a mathematical model used to identify and control formal languages. This model consists of a set of states, inputs, transitions, and outputs which can be employed to depict the behaviour of a machine that processes verbal input. An FSM goes through symbols from an alphabet one at a time, transitioning from one state to another in agreement with a set of transition rules that decide how it responds to each symbol. It can be used to recognize and generate language strings, as well as to determine if a string is part of a certain language. There are various types of finite automata like deterministic finite automata (DFA), nondeterministic finite automata (NFA), and pushdown automata (PDA) with distinct capabilities and restrictions.



## Objectives:


* Get familiar with formal languages, regular grammars & finite automata.
* Implement functionality for regular grammars and finite automata.
* Showcase the execution of the program.


## Implementation description

* About 2-3 sentences to explain each piece of the implementation.


* Code snippets from your files.
the word generating function
```
grammar = {
    "S": ["aP", "bQ"],
    "P": ["bP", "cP","dQ","e"],
    "Q": ["eQ", "fQ","a"]

def generate_word(grammar, start_symbol):
    word = "S"
    current_symbol = start_symbol
    while True:
        if current_symbol not in grammar:  # if current symbol is terminal
            word += current_symbol  # add to the word
            current_symbol = "end"
            if not word:  # if the word is empty, return None
                return None
            if len(word) > 10:  # if word is too long, return None
                return None
            if current_symbol == "end":  # if end symbol is reached, return the word
                word = word.replace("end","")
                return word[:-1]  # remove the end symbol

        else:
            rhs = random.choice(grammar[current_symbol])  # choose a random rule
            word = word.replace(current_symbol,rhs[0])
            for symbol in rhs[1:]:
                word += symbol
            current_symbol = word[-1]  # set current symbol to the last character in the word
 ```
 the automaton creating code 
 ```
 def create_automaton(grammar):
    # Step 1: Define the states of the automaton
    states = set([rule[0] for rule in grammar])

    # Step 2: Define the transitions between states
    transitions = {}
    for state in states:
        for rule in grammar:
            if rule[0] == state:
                if rule[1] == "":
                    # Epsilon transition
                    if state in transitions:
                        transitions[state].append((rule[2], None))
                    else:
                        transitions[state] = [(rule[2], None)]
                else:
                    # Regular transition
                    if state in transitions:
                        transitions[state].append((rule[2], rule[1]))
                    else:
                        transitions[state] = [(rule[2], rule[1])]

    # Step 3: Identify the start state of the automaton
    start_state = grammar[0][0]

    # Step 4: Identify the accepting states of the automaton
    accepting_states = set()
    for state in states:
        for rule in grammar:
            if rule[0] == state and rule[1] == "":
                accepting_states.add(state)

    # Construct the automaton
    automaton = {"states": states,
                 "transitions": transitions,
                 "start_state": start_state,
                 "accepting_states": accepting_states}

    return automaton
```
 
 
 the checking mechanism that checks the word to the automaton created
```
def accepts(automaton, word):
    current_state = automaton['start_state']
    for char in word:
        exists = False
        for symbol in automaton['transitions'][current_state]:
            if char == symbol[0]:
                current_state = symbol[1]
                exists = True

        if current_state is None:
            print(f"{word} is in this grammer")

        elif exists == False:
            # The current state does not have a transition on the current character
            print(f"{word} is not in this grammer")
            break
```



## Conclusions / Screenshots / Results
in this laboratory work i learned what's an automaton and how to implement them in code which was the most diffecult part and how to generate words in code and how to create it, i had some help and had to rewrite the code a couple of times but i got it working eventually, i hope i learned smth at least and looking forword to next lab.

## reuslts:
the automaton created:
{'states': {'S', 'P', 'Q'}, 'transitions': {'S': [('a', 'P'), ('b', 'Q')], 'P': [('b', 'P'), ('c', 'P'), ('d', 'Q'), ('e', None)], 'Q': [('e', 'Q'), ('e', 'Q'), ('f', 'Q'), ('a', None)]}, 'start_state': 'S', 'accepting_states': {'P', 'Q'}}

here are 5 words from given grammer
ace
befa
accbbbdea
None
ae

ace is in this grammer
ohno is not in this grammer
