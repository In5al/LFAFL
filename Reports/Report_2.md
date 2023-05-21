# Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

## University: Technical University of Moldova

## Course: Formal Languages & Finite Automata

### Author: Carp Dan-Octavian
----

## Theory
* A finite state machine (FA) is a computational model that examines an input string to see if it belongs to a particular language. It consists of nodes representing states, edges representing transitions, and specified initial and final states. Based on the input, the FA traverses the nodes and edges and decides to accept or reject. To turn a finite state machine (FA) into a grammar, we focus on transitions within the state machine. A non-terminal variable in the grammar corresponds to the state of the FA. Connections are represented by values on transitions (labels on edges). The initial state of FA is indicated by an arrow and the final state is represented by a circle. By analyzing these components, we can set production rules and construct a grammar that produces the same language as FA.

* The main difference between deterministic finite automata (DFA) and non-deterministic finite automata (NFA) is that in DFA each node (non-terminal variable) has only one transition to the next state for each terminal variable. In contrast, the NFA is to: There may be multiple transitions, even epsilon transitions (transitions that consume no input). To convert a nondeterministic finite state machine (NDFA) to a DFA, we need to create an equivalent DFA that understands the same language. It does this by considering all possible combinations of states in the NDFA and determining the appropriate next state based on the input symbols.

* The Chomsky hierarchy classifies formal grammars and languages into four types. Type 0 represents an unbounded grammar that can generate any language. Type 1 represents context-sensitive grammars used to model natural language syntax. Type 2 represents context-free grammars widely used in programming languages. Type 3 represents regular grammars used in regular expressions and pattern matching. Each type is more limited in power generation than the previous one. 
* The powerset construction algorithm is a technique to generate all possible subsets of a given set. It works by starting with an empty set and gradually adding each element of the original set to each existing subset, creating new subsets along the way.

## Objectives:

* Provide a function in your grammar type/class to classify the grammar based on the Chomsky hierarchy.
* Implement the conversion algorithm to transform a finite automaton (FA) into a regular grammar.
* Determine if the given FA is deterministic or non-deterministic.
*  Develop functionality to convert a nondeterministic finite automaton (NDFA) to a deterministic finite automaton (DFA).


## Implementation description
```
def classify_grammar(grammar):
    is_regular = True
```
To classify the grammar according to the Chomsky hierarchy, a function called classify_grammar was created in the grammar file. This function takes the grammar (production table) as input and determines its classification by comparing it against the rules of each grammar type.
```
        for production in grammar[nonterminal]:
            if len(production) > 2:
                is_regular = False
                break             
```

At this moment we check each production rule for a specific nonterminal in the grammar and sets the is_regular flag to False if any production rule has a   length greater than 2, breaking the loop.               
```
            if len(production) == 2:
                if (production[0].islower() and production[1].islower()) or (production[0].isupper() and production[1].isupper()):
                    is_regular = False
                    break
```
Additionally code sets the is_regular flag to False and breaks the loop if a production rule has a length of 2 and both symbols in the rule are either both lowercase letters (terminals) or both uppercase letters (nonterminals).In both cases it results that we are not dealing with regular grammar so we check if it's part of the other types.To note that it starts as Regular as it is the most restrained type and we slowly are making our way to Unrestricted Grammar
```
        for production in grammar[nonterminal]:
            if len(production) < len(nonterminal) or len(nonterminal) < 2:
                is_context_sensitive = False
                break
```
As we verify for the second type here we set the is_context_sensitive flag to False and break the loop if a production rule has a length smaller than the length of the nonterminal or if the length of the nonterminal itself is less than 2. This indicates that the grammar does not satisfy the conditions of a context-sensitive grammar.
```
        if not is_context_sensitive:
            break
    if is_context_sensitive:
        return "Type 2: Context-free grammar"
```
Now if the is_context_sensitive flag is False, meaning that at least one production rule did not satisfy the conditions(but they both confirm if it's of a Type 2), then we break the loop. But, if the flag remains True after checking all the production rules, then e can assumme that we have Type 1 known as a Context-Free grammar 
```
is_context_free = True
    for nonterminal in grammar:
        if len(nonterminal) > 1:
            is_context_free = False
            
 ```
 We continue to add more conditions so that we would know how to classify our grammar here we initialize the is_context_free flag as True. It then iterates through each nonterminal in the grammar. If a nonterminal has a length greater than 1, it means that the grammar does not satisfy the conditions of a context-free grammar. In this case, the is_context_free flag is set to False, indicating that the grammar is not context-free.But that doesnt't mean it is Context Sensitive either
 ```
    if is_context_free:
        return "Type 1: Context-sensitive grammar"
```
If the is_context_free flag is True, which implies that all nonterminals have a length of 1, then we have a Context-Sensitive-Grammar and that is confirmed by the return message. So we see that the program checks at every level what type of grammar we have it can become more restrained or less 
```
 If none of the above conditions are met, the grammar is an unrestricted grammar
    return "Type 0: Unrestricted grammar"
```

And laslty, if not a single requiremt is met, which means that not a single classification was fitted for our grammar, then we have a Type 0,known as Unrestricted Grammar.So we return that.

* to convert the FA back to a grammer i added a the function "fa_to_grammer"(in the automaton file) that takes the automaton as an atr and converts into a grammer by looking at the transactions and taking every state and deriving it to the production first and secound element and to just the first if it's a terminal state.
we take the transition table from the automaton as an attribute and use it to create the production table(grammer) as we take every nonterminal from the transitions and pair it with the left side one by one
```
grammer = []
    for state in automaton['transitions']:
        num = 0
        for transition in automaton['transitions'][state]:
            if automaton['transitions'][state][num][1] == None:
                grammer.append(state + " -> " + automaton['transitions'][state][num][0])
            else:
                grammer.append(state + " -> " + automaton['transitions'][state][num][0] + automaton['transitions'][state][num][1])
            num = num + 1

    return grammer
```

* after that i implemented the nfa to dfa conversion algorithm using the powerset construction alogrithm in the function nfa_to_dfa that takes the nfa and the start state as atributes and generates a dfa using the new class FA that constructs FA's for convinient use.
first we need to calculate epsilon closoure so we take the start symbol and look for any epsilon transaction in the nfa and return the start symbol or the combination(frozenset) of symbols
```
 closure = set(states)
    queue = list(states)
    while queue:
        curr_state = queue.pop(0)
        for next_state in nfa.transitions.get((curr_state, None), []):
            if next_state not in closure:
                closure.add(next_state)
                queue.append(next_state)
    return frozenset(closure)
```
then starting from the start symbol that we calculated with the epsilon closure we start to go through each symbol and go through the transitions adding every new symbol or frozenset to the symbols and checking every combination until the last symbol.
```
# Process the remaining states of the DFA
    queue = [dfa_start_state]
    while queue:
        curr_state = queue.pop(0)

        # Compute the transitions from the current state on each input symbol
        for symbol in nfa.alphabet:
            next_states = set()
            for state in curr_state:
                next_states |= set(nfa.transitions.get((state, symbol), []))
            next_states = epsilon_closure(nfa, next_states)

            if next_states:
                # Add the new state and transition to the DFA
                if next_states not in dfa_states:
                    dfa_states.add(next_states)
                    if any(state in nfa.accept_states for state in next_states):
                        dfa_accept_states.add(next_states)
                    queue.append(next_states)
                dfa_transitions[(curr_state, symbol)] = next_states
 ```
 then we construct the new DFA from the new transitions without the epsilon transitions
 ```
 # Create the DFA object
    dfa = FA(dfa_states, nfa.alphabet, dfa_transitions, dfa_start_state, dfa_accept_states)
    return dfa
```
* to determine if the FA is deterministic or not i implemented a methode in the automaton file that checks if the automaton has duplicated transitions or epsilon transition from each state.
```
    for state in automaton['transitions']:
        for production in automaton['transitions'][state]:
            if production[0][0] == '':
                return False
            num = 0
            for _ in automaton['transitions'][state]:
                if production[0][0] == _[0][0]:
                    num = num + 1
                    if num == 2:
                        return "the FA isn't deterministic"
    return "the FA is deterministic"
```
* i tried implementing the graphical presentation using visual_automata library but i kept giving me an infinite automaton error although it reaches all the end states normally so i just printed all the vertices and nodes in the terminal
```
digraph G {
rankdir=LR;
S [fillcolor="#66cc33", style=filled];
Q [peripheries=2];
P [peripheries=2];
S -> P  [label=a];
S -> Q  [label=b];
Q -> Q  [label=e];
Q -> Q  [label=f];
Q -> Q  [label=a];
P -> P  [label=b];
P -> P  [label=c];
P -> Q  [label=d];
P -> P  [label=e];
}
```

* for testing i created 4 additional grammers to check the classify methode and for the dfa to grammer methode i generated the new grammer and compared it to the original one in the main file should be all the testing code and the results presented in the terminal if run
```
nfa = FA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_accept_states)

dfa = nfa_to_dfa(nfa, 'q0')
print("the productions of the DFA")
print(dfa.transitions)
print("\nthe original grammer is: " + classify_grammar(grammar))
print("the first grammer is: " + classify_grammar(grammer))
print("the secound grammer is: " + classify_grammar(grammer1))
print("the third grammer is: " + classify_grammar(grammer2))

print("\n" + Is_DFA(automaton))
```

## Conclusions / Screenshots / Results
in this lab i learned more about the NFA and DFA automatons and the main defirences between them and how to convert an NFA into a DFA in code (which wasn't easy) and learned more about every type in the chomsky hierchy and some interesting external libraries that have all this implemented that can be easly used.

## Output:
```

 the set of productions of the generated grammer
['D -> bE', 'L -> aL', 'L -> bL', 'L -> c', 'S -> aD', 'E -> cF', 'E -> dL', 'F -> dD']
True
equal to the original

the productions of the DFA
{(frozenset({'q0'}), 'a'): frozenset({'q1'}), (frozenset({'q1'}), 'a'): frozenset({'q1'}), (frozenset({'q1'}), 'b'): frozenset({'q2'}), (frozenset({'q2'}), 'b'): frozenset({'q3', 'q2'}), (frozenset({'q3', 'q2'}), 'a'): frozenset({'q1'}), (frozenset({'q3', 'q2'}), 'b'): frozenset({'q3', 'q2'})}

the original grammer is: Type 3: Regular grammar
the first grammer is: Type 2: Context-free grammar
the secound grammer is: Type 1: Context-sensitive grammar
the third grammer is: Type 0: Unrestricted grammar

the FA is deterministic
```
