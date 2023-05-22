# Chomsky Normal Form

# Intro to formal languages. Regular grammars. Finite Automata.

## University: Technical University of Moldova

## Course: Formal Languages & Finite Automata

### Author: Carp Dan-Octavian

#### Variant: 7
----

## Theory
Chomsky Normal Form (CNF) serves as a standardized way to represent context-free languages, offering several benefits in terms of understanding and generating strings using this type of grammar. To achieve CNF, there are two primary requirements:

Production rules in the grammar must follow one of two specific forms: either N -> t or N -> NN. Here, "N" represents a nonterminal symbol, while "t" represents a terminal symbol.

Prior to applying CNF, the grammar needs to undergo a normalization process. This involves ensuring the following:
a. No epsilon productions exist, where a production rule leads to an empty string.
b. No unit productions are present, where a nonterminal directly produces another nonterminal.
c. No nonproductive or inaccessible symbols are within the grammar, meaning every nonterminal can eventually derive a string of terminals.


## Objectives:

1. Learn about Chomsky Normal Form (CNF) [1].
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
    1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    2. The implemented functionality needs executed and tested.
    3. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
    4. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.

## Implementation description
```
class ChomskyNormalForm:
    def __init__(self, VN, VT, P, S):
        self.VN = VN
        self.VT = VT
        self.P = P
        self.S = S
```
First we define the grammar.We create a class called `ChomskyNormalForm`.This class has an initilization method `init` which takes four parameters `VN`, `VT`, `P`, and `S` where: <br>
* VN represents the set of nonterminal symbols <br>
* VT represents the set of terminal symbols  <br>
* P is the set of production rules defining the grammar.Each production rule specifies how nonterminals can be replace by combinations of terminals and nonterminals <br> 
* S is the start symbol of the grammar indicating where the derivation should start 
```
V_N = ['S', 'A', 'B', 'C', 'E']
V_T = ['a', 'b']
P = {'S': ['bA', 'B'],
     'A': ['a', 'aS', 'bAaAb', 'b'],
     'B': ['AC', 'bS', 'aAa'],
     'C': ['AB', 'epsilon'],
     'E': ['BA']
}
S = 'S'

grammar = ChomskyNormalForm(V_N, V_T, P, S)
```
I initilialize a `ChomskyNormalForm` object with the nonterminal symbols according to  my variant followed by the terminals symbols, the production rules and the start symbol. I then pass the given nonterminal symbols, terminal symbols, production and start symbol into the `ChomskyNormalForm`. Now this object can be used to work with and manipulate the grammar components

Befote we can proceed and transform our grammmar into `ChomskyNormalForm` we first need to normalize it and the fisrst sept into doing that is to get rid of the epsilon production 
```
    def eliminate_epsilon(self):
        P = self.P.copy()
        eps_productions = [sym for sym in P if '' in P[sym]]
        new_productions = {}
```
* we begin by defining a method `eliminate_epsilon` within `ChomskyNormalForm` class.This method begins by creating a copy of the production rules `P` by using `P = self.P.copy()`.This way we make sure that the original production rules remain the same during the elimination of epsilon production. <br>
* Next we identify the epsilon productions by iterating over the nonterminal symbols in `P` using a list comprehension `eps_productions = [sym for sym in P if '' in P[sym]]`. Here, each nonterminal symbol `sym` is checked to see if it has an epsilon production(an empty string) in the list of production rules <br>
* And then, an empty dictionary named `new_productions` is initialized. This will store the updated production rules after we finish with epsilon elimination <br> 
```      
        for sym in P:
            new_productions[sym] = [p for p in P[sym] if p != '']
            for i, p in enumerate(new_productions[sym]):
```
* Here we begin by itterating over each nonterminal symbol `sym` in the original production rules `P` using the `for sym in P` loop.
* For each nonterminal symbol we filter out any epsilon productions (empty strings) from the list of production rules associated with that symbol. This is done by constructing a new list comprehension: `new_productions[sym] = [p for p in P[sym] if p != '']`.We proceed by creating a list of production rules for the current nonterminal symbol without the epsilon productions.
* Then, within the same loop we continue to  processes the updated list of production rules for the current nonterminal symbol `new_productions[sym]` We use the `enumerate` function to iterate over each production rule, providing both the index `i` and the production rule itself 
```
                   for j in range(len(p)):
                    if p[j] in eps_productions:
                        for eps_prod in self.combine_epsilon(P[p[j]]):
                            new_productions.setdefault(sym, []).append(p[:j] + eps_prod + p[j + 1:])
        self.P = new_productions]
```
Here we iterate over each production rule for each nonterminal symbol. If a symbol in a production rule is identified as having an epsilon production , we combine the epilon production with the surronding symbols and we add the new production rule to theupdated `new_productions` dictionary. It ends by assigning the updated `new_productions` dictionary to the P attribute of the object.


After getting rid of epsilon production rhe next step is to get rif od unit production
```
                def eliminate_unit(self):
        for production in self.P:
```
We introduce a new method called `eliminate_unit` here the code begins to iterate through each production in the grammar's production rules `self.P`. Put it simply, it examines each rules one by one to perform the necesary operations 
```
            for symbol in self.P[production]:
                if symbol in self.VN:
                    self.P[production].remove(symbol)
                    self.P[production].extend(self.P[symbol])
```
* Within each production rule in self.P, the code goes on to check each symbol. If a symbol is identified as a non-terminal (a member of self.VN, which represents the set of nonterminal symbols)

* Firstly, the code removes the non-terminal symbol (symbol) from the production rule using the remove method 

* Then we extend the production rule by adding all the productions that can be derived from the removed non-terminal symbol. We do this by using `self.P[symbol]` to access the list of production rules associated with the non-terminal symbol and adding them to the current production rule using the extend method.

* By doing this we  expand the production rule, incorporating all the possible derived productions from the removed non-terminal symbol.



Once we are done with the unit production it's time we have to remove the non productive and inaccessible symbols. The`eliminate_nonproductive_inaccessible` method is going to take the job.
```
           def eliminate_nonproductive_inaccessible(self):
        reached = set()
        unreached = self.VN.copy()
        reached.add(self.S)
```
We start by creating an empty set called reached to keep track of the symbols that can be `reached` from the start symbol. Additionally, we create a copy of the set of nonterminal symbols `self.VN` and assign it to the set `unreached`.
 
Now, we take a decisive step by ensuring that the start symbol `self.S` is marked as reached. We add it to the `reached` set, indicating that it is accessible and can be derived from the start symbol.
```
        while True:
            changed = False
            for sym in self.P:
 ```  
 The code iterates over each symbol `sym` in the production rules `self.P`.
 
 Now we enter in a while True loop, indicating that it will continue executing until a specific condition is met
 
 This loop allows us to iterate through all the symbols in the production rules repeatedly, enabling us to make necessary changes or updates until we achieve the desired outcome.
   
By looping through the symbols, we can carefully analyze and manipulate the grammar to eliminate nonproductive and inaccessible symbols. The loop ensures that we cover all the symbols in the grammar, making it a vital part of the elimination process.  
 ```
                if sym in unreached:
                    for prod in self.P[sym]:
                        if all(s in reached or s in self.VT for s in prod):
                            unreached.remove(sym)
                            reached.add(sym)
                            changed = True
                            break
 ```                           
 First, the code checks if the current symbol (sym) is in the set of unreached symbols (unreached). If it is, it proceeds to the next step.  
 
 For each production rule associated with the current symbol (prod in self.P[sym]), the code performs a check. It ensures that all the symbols (s) in the production rule are either already reached symbols (s in reached) or terminal symbols (s in self.VT). 
 
 If all symbols in the production rule meet the criteria, it marks progress by removing the current symbol from the set of unreached symbols `unreached.remove(sym)` and adding it to the set of reached symbols `reached.add(sym)`. It also sets the changed variable to `True`, indicating that a change has occurred.
 ```
                if changed:
                    break
            if not changed:
                break
```
After iterating through all the symbols in the production rules and performing the necessary operations, the code checks if any changes were made `if changed`. If changes were made, it means that at least one nonproductive or inaccessible symbol was identified and processed.

In such a case, the code breaks out of the inner for loop using the break statement. This jump breaks the current iteration and restarts the loop from the beginning, allowing for another round of symbol analysis and potential updates

However, if no changes were made after a full iteration over all symbols, it signifies that all nonproductive and inaccessible symbols have been identified and processed. Thus, the code breaks out of the outer while True loop as well, using another `bbreak` statement
```

        nused = unreached
        for sym in nused:
            del self.P[sym]
            self.VN.remove(sym)
            if sym == self.S:
                self.S = None
        self.VT = set(t for prod in self.P.values() for s in prod for t in s if t not in self.VN)
```
We create a new variable called `nused` and assigns it the value of the `unreached` set. Wehis set contains symbols that are determined to be nonproductive and inaccessible.

Next we iterates over each symbol (sym) in the `nused` set

next i delete the inaccesable symbols ( i don't need to mark these ones as we delete the whole production group and because they're inaccesable that means they're not in any other production)

For each symbol we

1. delete the symbol (sym) from the production rules dictionary (self.P) using del self.P[sym]. This removes all the production rules associated with the symbol.

2. remove the symbol (sym) from the set of nonterminal symbols (self.VN) using self.VN.remove(sym)

3. If the symbol (sym) is the same as the start symbol (self.S),  we set the start symbol to None (self.S = None). This is done to handle the case where the start symbol is nonproductive or inaccessible.

Finally, the code updates the set of terminal symbols (self.VT) by reconstructing it. It iterates over the production rules, extracting all symbols (t) that are not in the set of nonterminal symbols (self.VN). These symbols are considered terminals. The resulting set of terminals is assigned back to self.VT.
```
self.VN.append('S0')
        dict = {'S0': ['S']}
        self.P = {**dict, **self.P}
```
Firstly, the code appends a new symbol 'S0' to the list of nonterminal symbols (self.VN). This symbol is added to indicate a new start symbol for the grammar

Next, a dictionary called dict is created with 'S0' as the key and ['S'] as the associated value. This dictionary represents the production rule for the new start symbol, where 'S0' derives to 'S'.


Lastly we update the production rules (self.P) by combining the dict dictionary with the existing production rules. This is achieved using the ** operator, which performs dictionary unpacking. It merges the dict dictionary with the self.P
```
final = {}
        dict = {}
        flag = 0
        for production in self.P:
            for symbol in self.P[production]:
                if len(symbol) > 1:
                    for char in symbol:
                        if char in self.VT and char not in final.values():
                            final[chr(70 + flag)] = char
                            dict[char] = chr(70 + flag)
                            flag += 1

        for item in dict.keys():
            for production in self.P:
                for i in range(len(self.P[production])):
                    if len(self.P[production][i]) > 1:
                        self.P[production][i] = self.P[production][i].replace(item, dict[item])
```
To keep track of all new non-terminal symbols and their corresponding productions, it builds a dictionary. The process then repeats for each production that has more than two symbols across all of the products.
```

## Conclusions / Screenshots / Results
After completing this laboratory work, I learnt how to convert CFG into CNF. In order to complete all the necessary steps and observe the immediate results, I implemented different functions.

## Output

After running the project I got the following results:
```
---------------------------------------------------------------------------------
Productions:
P = {'S': ['bA', 'B'], 'A': ['a', 'aS', 'bAaAb', 'b'], 'B': ['AC', 'bS', 'aAa'], 'C': ['AB', 'epsilon'], 'E': ['BA']}

Eliminate Epsilon:
{'S': ['bA', 'B'], 'A': ['a', 'aS', 'bAaAb', 'b'], 'B': ['AC', 'bS', 'aAa'], 'C': ['AB'], 'E': ['BA']}

Eliminate Unit Production:
{'S': ['bA', 'AC', 'bS', 'aAa'], 'A': ['a', 'aS', 'bAaAb', 'b'], 'B': ['AC', 'bS', 'aAa'], 'C': ['AB'], 'E': ['BA']}

Eliminate Innaccesible:
{'S': ['bA', 'AC', 'bS', 'aAa'], 'A': ['a', 'aS', 'bAaAb', 'b'], 'B': ['AC', 'bS', 'aAa'], 'C': ['AB'], 'E': ['BA']}

Chomsky Normal Form:
X1 -> GA
P = {'S0': ['S'], 'S': ['FA', 'AC', 'FS', 'Y'], 'A': ['a', 'GS', 'b', 'Y'], 'B': ['AC', 'FS', 'Y'], 'C': ['AB'], 'E': ['BA'], 'F': 'b', 'G': 'a', 'X1': 'GA'}
---------------------------------------------------------------------------------
```


