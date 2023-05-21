# Intro to formal languages. Regular grammars. Finite Automata.
## University: Technical University of Moldova
## Course: Formal Languages & Finite Automata
### Author: Carp Dan-Octavian

----

## Theory
Formal languages are sets of finite-length sequences of symbols constructed according to well-defined grammar rules. These languages describe programming languages and other language types. Grammar defines how symbols are combined to form valid strings using production rules. Different types of grammars, such as regular and context-free grammars, capture different language complexities. Grammar plays a crucial role in formal language theory, enabling analysis of language structure and behavior.

Finite state machines (FSMs) are mathematical models for recognizing and controlling formal languages. FSMs process symbols sequentially, transitioning between states based on rules. They can recognize, generate, and determine membership in a language. Various types of FSMs, such as deterministic and nondeterministic finite automata, have different capabilities. FSMs are essential for language processing and algorithm development.



## Objectives:


* Get familiar with formal languages, regular grammars & finite automata.
* Implement functionality for regular grammars and finite automata.
* Showcase the execution of the program.


## Implementation description

```
grammar = {
    "S": ["aD"],
    "D": ["bE"],
    "E": ["cF", "dL"],
    "F": ["dD"],
    "L": ["aL","bL","c"]
}
```
* Here we define the grammar rules for our language. We begin by defining the start symbol "S" . It generates a sentence with a non-terminal "D" following a terminal 'a'.The non-terminal "D" generates a terminal 'b' followed by a non-terminal "E".The non-terminal "E" can generate either a terminal 'c' followed by non-terminal "F" or a terminal 'd' followed by non-terminal "L".The non-terminal "F" generates a terminal 'd' followed by non-terminal "D".The non-terminal "L" can generate itself recursively (left recursion) or a terminal 'c'

```
def generate_word(grammar, start_symbol):
    word = "S"
    current_symbol = start_symbol
    while True:
 ```
 We define a function to generate a word based on a given grammar and start symbol. We start by initializing the word with the start symbol then we set the current symbol to the start symbol.We repeat until a word is generated or the process is terminated:
 ```
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
```
If the current symbol is a terminal then we: <br /> 
1.Add it to the word <br />
2.Set current symbol as "end" to indicate reaching the end of the word <br />
3.If the word is empty, return None <br />
4.If the word is too long, return None <br />
5.If the end symbol is reached, return the word <br />
6.Remove the "end" symbol <br />
7.Remove the last character (which was "end")
```
        else:
            rhs = random.choice(grammar[current_symbol])  # choose a random rule
            word = word.replace(current_symbol,rhs[0])
            for symbol in rhs[1:]:
                word += symbol
            current_symbol = word[-1]  # set current symbol to the last character in the word
 ```
 If the current symbol is a non-terminal then we: <br />
 1.Choose a random rule from the grammar <br />
 2.Replace the current symbol in the word with the first character of the chosen rule <br />
 3.Add the remaining symbols of the rule to the word <br />
 4.Set the current symbol to the last character in the word <br />
 ```
 def create_automaton(grammar):
    states = set([rule[0] for rule in grammar])
 ```
 Here we define a function to create an automaton based on a given grammar.We start by defining the states of the automaton.We create a set of states by extracting the first element of each rule in the grammar
 ```
 
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
                        
```
 In the next step we define the transitions between states. We start by initializing an empty dictionary to store the transitions. We then iterate over each state.In the second for we iterate over each rule in the grammar.We check if the first element of the rule matches the current state. In the second if we check if the second element of the rule is an empty string, it represents an epsilon transition. We verify if the current state already exists in the transitions dictionary, if it exists we append the target state and None (representing epsilon) to the existing list of transitions for the current state otherwise we create a new list with the target state and None as the transition and add it to the transitions dictionary. Now if it's a regular transition then first we check if the current state already exists in the transitions dictionary. If it does then we append the target state and the second element of the rule to the existing list of transitions for the current state. If not then we create a new list with the target state and the second element of the rule as the transition and add it to the transitions dictionary.
```

    # Step 3: Identify the start state of the automaton
    start_state = grammar[0][0]

```
We continue by identifing the start state of the automaton.We assign the first symbol of the first rule in the grammar as the start state of the automaton
start_state = grammar[0][0]
```
    # Step 4: Identify the accepting states of the automaton
    accepting_states = set()
    for state in states:
        for rule in grammar:
            if rule[0] == state and rule[1] == "":
                accepting_states.add(state)
 ```
 This part involves identifying the accepting states of the automaton.It further explains how an empty set is initialized, and then, for each state in the set of states, we check if any rule in the grammar matches the current state as the first symbol and an empty string as the second symbol. If there is a match, the current state is added to the set of accepting states.

 ```

    # Construct the automaton
    automaton = {"states": states,
                 "transitions": transitions,
                 "start_state": start_state,
                 "accepting_states": accepting_states}

    return automaton
```
 Finally, an automaton dictionary is constructed using the identified states, transitions, start state, and accepting states, which is then returned as the result.
```
def accepts(automaton, word):
    current_state = automaton['start_state']
    
 ```
 We also define a function to check if an automaton accepts a given word.We start by setting the current state to the start state of the automaton
 ```
    for char in word:
        exists = False
        for symbol in automaton['transitions'][current_state]:
            if char == symbol[0]:
                current_state = symbol[1]
                exists = True
```
We begin by iterating over each character in the word.First we initialize a boolean variable to track if a transition exists for the current character. Next we iterate over the symbols in the transitions for the current state, if the current character matches the first symbol of the transition then we set the current state to the next state indicated by the transition we also set the exists variable to True to indicate that a transition exists for the current character
```
        if current_state is None:
            print(f"{word} is in this grammer")
```
If the current state is None, then we print that the word is in the grammar
```

        elif exists == False:
            # The current state does not have a transition on the current character
            print(f"{word} is not in this grammer")
            break
```
And finally if exists is still False,meaning that no transition exists for the current character,then we print that the word is not in the grammar and exit the loop


## Conclusions / Screenshots / Results
This lab focused on grammars and automata. We started by defining a grammar with production rules for generating words. We then used the grammar to identify the states and transitions of the automaton and created the automaton.

To check if the automaton accepts a particular word, I implemented a function that iterates over each letter in the word. Find valid transitions in the current state and update the state accordingly. If the loop completes without reaching the accepting state, it means the word is not in the grammar.

There were comments explaining the purpose and logic behind each step.

In this lab, we started working with grammars and automata and demonstrated their application in word generation and acceptance testing. Understanding these concepts is essential for students interested in formal languages ​​and computational linguistics. 

## Final Results:
```
{'states': {'F', 'E', 'D', 'L', 'S'}, 'transitions': {'F': [('d', 'D')], 'E': [('c', 'F'), ('d', 'L')], 'D': [('b', 'E')], 'L': [('a', 'L'), ('b', 'L'), ('c', None)], 'S': [('a', 'D')]}, 'start_state': 'S', 'accepting_states': {'L'}}

here are 5 words from given grammar
abdabac
abdc
abdc
abdaac
abdbbbbc

lamda is not in this grammer
abcdbdc is in this grammer
```

"abdabac" - This word is not in the grammar.

"abdc" - This word is in the grammar.

"abdc" - This word is in the grammar as well.

"abdaac" - This word is not in the grammar.

"abdbbbbc" - This word is in the grammar.
