from Source.Grammar.grammer import *
from Source.Automaton.automaton import *
from Source.Grammar.lexer import *
from visual_automata.fa.dfa import VisualDFA
import visual_automata
from visual_automata.fa.nfa import *
from automata.fa.dfa import DFA
import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
# Define the regular grammar
grammar = {
    "S": ["aD"],
    "D": ["bE"],
    "E": ["cF", "dL"],
    "F": ["dD"],
    "L": ["aL","bL","c"]
}
grammar1 = [("S","D","a"),("D","E","b"),("E","F","c"),("E","L","d"),("F","D","d"),
            ("L","L","a"),("L","L","b"),("L","","c")]

automaton = create_automaton(grammar1)
print("the automaton based on the given grammar")
print(automaton)

print("\nhere are 5 words from given grammar")
for _ in range(5):
    word = generate_word(grammar,"S")
    print(word)
print("")

accepts(automaton,"lamda")
accepts(automaton,"abcdbdc")
'''
Lab2
'''
grammar2 = [
    "S -> aD",
    "D -> bE",
    "E -> cF",
    "E -> dL",
    "F -> dD",
    "L -> aL",
    "L -> bL",
    "L -> c"
]
grammar3 = fa_to_grammar(automaton)
print("\n the set of productions of the generated grammer")
print(grammar3)

equal = True
for production in grammar3:
    if production in grammar2:
        equal = True
    else:
        equal = False
print(equal)
print("equal to the original\n")

nfa_states = {'q0', 'q1', 'q2', 'q3'}
nfa_alphabet = {'a', 'b'}
nfa_transitions = {
    ('q0', 'a'): {'q1'},
    ('q1', 'a'): {'q1'},
    ('q1', 'b'): {'q2'},
    ('q2', 'b'): {'q2', "q3"},
    ('q3', 'a'): {'q1'}
}
nfa_start_state = 'q0'
nfa_accept_states = {'q3'}

nfa = FA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_accept_states)

dfa = nfa_to_dfa(nfa, 'q0')
print("the productions of the DFA")
print(dfa.transitions)

grammer = {
    "Sa": ["aaB","bS"],
    "aB": ["bB"]
}
grammer1 = {
    "S": ["aaB","Sb"],
    "B": ["bS","b"]
}
grammer2 = {
    "aa": ["aB","ss"],
    "BAs":["aaB","s"],
    "sA": ["a","bbs"]
}
print("\nthe original grammer is: " + classify_grammar(grammar))
print("the first grammer is: " + classify_grammar(grammer))
print("the secound grammer is: " + classify_grammar(grammer1))
print("the third grammer is: " + classify_grammar(grammer2))

print("\n" + Is_DFA(automaton))


'''
Lab 3

'''
string = '''
public class Test {

   public static void main(String args[]) {
      int [] numbers = {10, 20, 30, 40, 50};
      // printing !
      for(int x : numbers ) {
         System.out.print( x );
         System.out.print(",");
      }
      System.out.print("\n");
      String [] names = {"James", "Larry", "Tom", "Lacy"};
      /*
      looping over 
      */
      for( String name : names ) {
         System.out.print( name );
         System.out.print(",");
      }
   }
}
'''

tokenize(string)
'''

Lab 4

'''
Vn = ['S','A','B','C','D','E']
Vt = ['a','b']
S = 'S'
P = {
    "S": ["aB", "AC"],
    "A": ["a", "ASC", "BC", "aD"],
    "B": ["b", "bS"],
    "C": [None],
    "D": ["abC"],
    "E": ["aB"]
}
grammar_1 = Grammar(S,Vn,Vt,P)

normalize(grammar_1)

