# Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

## University: Technical University of Moldova

## Course: Formal Languages & Finite Automata

### Author: Carp Dan-Octavian
----

## Theory
 There are 4 types of grammar according to Chomsky Classification: <p>
    
* Type 0 – Unrestricted
* Type 1 – Context-Sensitive
* Type 2 – Context-Free
* Type 3 – Regular

Automata can be used to recognize formal languages, for example described by grammars.
There are different types of automata that can describe different types of languages.
For example:

-   A finite automaton (NFA/DFA, state machine) can describe a regular grammar (type 3)
-   A pushdown automaton (PDA) can describe a context-free grammar (type 2)

A DFA is equivalent in power to an NFA, even though NFA&rsquo;s are more flexible hierarchy in terms of powers.

-   The conversion NFA -&gt; DFA can be done using the powerset construction.
-   The conversion regular grammar -&gt; NFA and viceversa is straightforward.
-   The conversion Grammar -&gt; DFA can&rsquo;t really be done directly,
    instead go through the steps: Grammar -&gt; NFA -&gt; DFA.
    
    **NFA and DFA**
*  A Finite Automata(FA) is said to be deterministic DFA if corresponding to an input symbol, there is a single resultant state, only one transition.
*  A Finite Automata(FA) is said to be non-deterministic NFA if there is more than one possible transition from one state on the same input symbol.


## Objectives:

1. Understand what an automaton is and what it can be used for.

2. Continuing the work in the same repository and the same project, the following need to be added:
    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.
    
    d. Represent the finite automaton graphically (Optional, and can be considered as a __*bonus point*__):
      
    - You can use external libraries, tools or APIs to generate the figures/diagrams.
        
    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.



## Implementation description
```
def classify_grammar(grammar):
    is_regular = True
```
To classify the grammar according to the Chomsky hierarchy, a function called `classify_grammar` was created in the grammar file. This function takes the grammar (production table) as input and determines its classification by comparing it against the rules of each grammar type.
```
        for production in grammar[nonterminal]:
            if len(production) > 2:
                is_regular = False
                break             
```

At this moment we check each production rule for a specific nonterminal in the grammar and sets the `is_regular` flag to False if any production rule has a   length greater than 2, breaking the loop.               
```
            if len(production) == 2:
                if (production[0].islower() and production[1].islower()) or (production[0].isupper() and production[1].isupper()):
                    is_regular = False
                    break
```
Additionally code sets the `is_regular` flag to False and breaks the loop if a production rule has a length of 2 and both symbols in the rule are either both lowercase letters (terminals) or both uppercase letters (nonterminals).In both cases it results that we are not dealing with regular grammar so we check if it's part of the other types.To note that it starts as Regular as it is the most restrained type and we slowly are making our way to Unrestricted Grammar
```
        for production in grammar[nonterminal]:
            if len(production) < len(nonterminal) or len(nonterminal) < 2:
                is_context_sensitive = False
                break
```
As we verify for the second type here we set the `is_context_sensitive` flag to False and break the loop if a production rule has a length smaller than the length of the nonterminal or if the length of the nonterminal itself is less than 2. This indicates that the grammar does not satisfy the conditions of a context-sensitive grammar.
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
 We continue to add more conditions so that we would know how to classify our grammar here we initialize the `is_context_free` flag as True. It then iterates through each nonterminal in the grammar. If a nonterminal has a length greater than 1, it means that the grammar does not satisfy the conditions of a `context-free grammar`. In this case, the `is_context_free` flag is set to False, indicating that the grammar is not context-free.But that doesnt't mean it is Context Sensitive either
 ```
    if is_context_free:
        return "Type 1: Context-sensitive grammar"
```
If the `is_context_free` flag is True, which implies that all nonterminals have a length of 1, then we have a Context-Sensitive-Grammar and that is confirmed by the return message. So we see that the program checks at every level what type of grammar we have it can become more restrained or less 
```
 If none of the above conditions are met, the grammar is an unrestricted grammar
    return "Type 0: Unrestricted grammar"
```

And laslty, if not a single requiremt is met, which means that not a single classification was fitted for our grammar, then we have a Type 0,known as Unrestricted Grammar.So we return that.
```
def fa_to_grammar(automaton):
```
To convert the  Finite Automata back to Grammar we introduced a new function and that is `fa_to_grammar`. We added it in the automaton file. The function converts a finite automaton back into a grammar representation. It accomplishes this by examining the transitions of the automaton and generating production rules based on the states. The function differentiates between terminal and non-terminal states when deriving the production rules

```
grammer = []
    for state in automaton['transitions']:
        num = 0
```
we begin by initializeing an empty list called "grammar" and a variable "num" with a value of 0.
```     
        for transition in automaton['transitions'][state]:
            if automaton['transitions'][state][num][1] == None:
                grammer.append(state + " -> " + automaton['transitions'][state][num][0])
 ```
 For each transition in the transitions of the given state, if the second element of the transition is None( meaning it's an epsilon transition),then we append a production rule to the "grammar" list, where the left-hand side is the current state and the right-hand side is the first element of the transition.

 ```                
            else:
                grammer.append(state + " -> " + automaton['transitions'][state][num][0] + automaton['transitions'][state][num][1])
            num = num + 1

    return grammer
```
And if the transitions where the second element is not None (an non-epsilon transitions), then we append a production rule to the "grammar" list. The left-hand side of the rule is the current state, and the right-hand side consists of concatenating the first and second elements of the transition.

After iterating through all the transitions, the function returns the "grammar" list containing the generated production rules.
```
def epsilon_closure(nfa, states):
 closure = set(states)
    queue = list(states)
```    
Then we have a function named epsilon_closure that takes an NFA and a set of states as input parameters.We initialize a "closure" set with the states, and a "queue" list with the same states
```
    while queue:
        curr_state = queue.pop(0)
```
Within each iteration of the loop, the `curr_state` variable is assigned the value popped from the front of the "queue" list using the pop(0) method. This means that the first element in the queue is removed and assigned to `curr_state` for further processing
```
        
        for next_state in nfa.transitions.get((curr_state, None), []):
            if next_state not in closure:
                closure.add(next_state)
                queue.append(next_state)
    return frozenset(closure)
```
 For each `next_state` in the list of transitions from the current state ("curr_state") with an epsilon symbol (None), the code checks if the `next_state` is not already in the "closure" set. If it is not in the "closure" set, the `next_state` is added to the "closure" set and appended to the "queue" list for further processing.



then starting from the start symbol that we calculated with the epsilon closure we start to go through each symbol and go through the transitions adding every new symbol or frozenset to the symbols and checking every combination until the last symbol.
```
# def nfa_to_dfa(nfa, start_state):
    dfa_states = set()
    dfa_transitions = {}
    dfa_start_state = frozenset([start_state])
    dfa_accept_states = set()
    
  ```
  And here we have the function that converts Nondeterministic Finite Automaton to Deterministic.We start by initializing an empty set called dfa_states to store the states of the DFA followed by an empty dictionary called `dfa_transitions` to store the transitions of the DFA.The `dfa_start_state` is set to a frozenset containing the start_state of the NFA while he `dfa_accept_states` is an empty set initially, which will later store the accept states of the DFA.
  ```
    

    # Compute the epsilon closure of the start state
    start_closure = epsilon_closure(nfa, dfa_start_state)
  ```
  The `start_closure` calls the `epsilon_closure` function, the function we previously analzised.The function has `nfa` and `dfa_start_state` as arguments. The function will computes the epsilon closure of the initial state of the DFA to determine the set of states reachable from the initial state through epsilon transitions.

  ```

    # Add the start state and its epsilon closure to the DFA
    dfa_states.add(dfa_start_state)
    if any(state in nfa.accept_states for state in start_closure):
        dfa_accept_states.add(dfa_start_state)
        
   ```
   `The dfa_start_state` is added to `dfa_states set`, indicating that it is one of the states in the DFA.We then if any state in the `start_closure` (epsilon closure of the initial state) is also present in the NFA's `accept_states`. If there is at least one matching state, it means that the DFA's initial state is an accept state, so it is added to the `dfa_accept_states` set.
   ```

    # Process the remaining states of the DFA
    queue = [dfa_start_state]
    while queue:
        curr_state = queue.pop(0)
```
Within each iteration of the loop, the `curr_state` variable is assigned the value popped from the front of the queue list using the pop(0) method. This means that the first element in the queue is removed and assigned to `curr_state` for further processing.
```

        # Compute the transitions from the current state on each input symbol
        for symbol in nfa.alphabet:
            next_states = set()
            for state in curr_state:
                next_states |= set(nfa.transitions.get((state, symbol), []))
            next_states = epsilon_closure(nfa, next_states)
 ```
 For each symbol in the NFA's alphabet, we initialize an empty set `next_states` to store the next states. It then iterates over each state in the `curr_state` set and retrieves the transitions for the current state and symbol using `nfa.transitions.get((state, symbol), [])`. The resulting states are added to the `next_states` set using the union operator `|=`.

After that, the `next_states` set is updated by computing its epsilon closure using the `epsilon_closure` function. This ensures that all epsilon transitions from the next states are included in the set.
 ```

            if next_states:
                # Add the new state and transition to the DFA
                if next_states not in dfa_states:
                    dfa_states.add(next_states)
 ```
 If the `next_states` set is not empty which tells us there are valid transitions for the current state and symbol, then w check if the `next_states` set is not already present in the `dfa_states set`. If it is not present, it means that this is a new state for the DFA, so it is added to  `dfa_states set`.
 ```
                    if any(state in nfa.accept_states for state in next_states):
                        dfa_accept_states.add(next_states)
                    queue.append(next_states)
                dfa_transitions[(curr_state, symbol)] = next_states

 ```
 If any state in the `next_states set` is present in the NFA's` accept_states`, it means that the DFA has reached an accept state, so the `next_states` set is added to the `dfa_accept_states` set.The `next_states` set is then appended to the queue list for further exploration.Finally, the DFA's transition from the `curr_state` to `next_states` for the current symbol is recorded in the `dfa_transitions` dictionary.
 
 then we construct the new DFA from the new transitions without the epsilon transitions
 ```
 # Create the DFA object
    dfa = FA(dfa_states, nfa.alphabet, dfa_transitions, dfa_start_state, dfa_accept_states)
    return dfa
```
We follow by creating  DFA object with the `dfa_states` as the set of states, `nfa.alphabet` as the alphabet, `dfa_transitions` as the transition table, `dfa_start_state` as the start state, and `dfa_accept_states` as the set of accept states.



to determine if the FA is deterministic or not we create a new method in the automaton file that checks if the automaton has duplicated transitions or epsilon transition from each state.
```
    for state in automaton['transitions']:
        for production in automaton['transitions'][state]:
            if production[0][0] == '':
                return False
            num = 0
```
This part iterates over each state in the automaton's transitions. For each state, it further iterates over each production in the transitions. It checks if the first character of the production's first element is an empty string (''). If it is, it means there is an empty transition, and the code returns False, indicating that the automaton is not valid.
```
            for _ in automaton['transitions'][state]:
                if production[0][0] == _[0][0]:
                    num = num + 1
                    if num == 2:
                        return "the FA isn't deterministic"
    return "the FA is deterministic"
```
Here it iterates over each production in the transitions of the current state. For each production, it compares the first character of its first element with the first character of the first element in the previously encountered productions. If they match, it means there are multiple transitions with the same input symbol from the current state, indicating non-determinism. In such a case, the code returns the message "the FA isn't deterministic".

If no non-deterministic transitions are found, the code returns the message "the FA is deterministic", indicating that the automaton is deterministic.

The code includes four additional grammars to verify the classification results As for dfa to grammer method we can check if it checks out and is proved to be like the original
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
In this lab, we explored NFA and DFA automatons, focusing on their differences and conversion processes. We learned to convert an NFA into a DFA and gained insights into the Chomsky hierarchy, which categorizes grammars. We implemented functions to classify grammars based on their Chomsky type and convert NFAs to regular grammars. Additionally, we examined determinism in automatons.

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
