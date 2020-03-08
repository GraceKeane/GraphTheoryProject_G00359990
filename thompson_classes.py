# Grace Keane - G00359990
# Bsc in Computing in Software Development
# Demonstrating the use of classes using python and Thompsons construction

class state:
    # Every state has 0, 1 or 2 edges
    # None = 0
    
    edges = []

    # Label for arrows, none means epsilon
    # Label is associated with the state
    label1 = None

    # Creating a constructor for the class
    def __init__(self, label=None, edges=[]):

        # Instances
        self.edges = edges
        self.label = label

# Fragments are a combination of states
# Fragment is an array with two things in it. Start = initial, end = except 
# For fragments you need to know initial state and except state 
class NFA_Fragments:

    # Member variabes

    # Start state of NFA fragment
    start = None
    # Accept state of NFA fragment
    accept = None

    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def shunt(infix):
    # Convert input to a stack list
    infix = list(infix)[::-1]

    # Operator stack
    opers = []

    # Output list
    postfix = []

    # Operator precidence * - . - |
    prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

    # Loop through the input one character at a time
    while infix:
        # Pop a character from the list
        c = infix.pop() # Removes the last element in infix as a list & returns whatever is poper off

        if c == '(':
            # Push an open bracket to the stack
            opers.append(c)
        elif c == ')':
            # Pop operators stack until open bracket is found
            while opers[-1] != '(':
                postfix.append(opers.pop())

             # Remove open bracket
            opers.pop()

        elif c in prec:
            # Push the operator stack until you find an open bracket
            while opers and  prec[c] < prec[opers[-1]]:
            # Push c to the operator stack with higher precidence to the output
                postfix.append(opers.pop())
            opers.append(c)
        else:
            # Typically we just push the character to the output
            postfix.append(c)

    # Pop all operators to the output
    while opers:
        postfix.append(opers.pop())

    # Convert output list to string
    return ''.join(postfix)

def regex_compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix) [::-1]

    # Keep track of fragments created from postfix regex
    nfa_stack = []

    # Creating nfa that matches post regex that represents regex
    while postfix:
        # Pop a carracter from postfix
        c = postfix.pop()

        if c == '.':
            # Pop two fragments off the stack
            fragment1 = nfa_stack.pop()
            fragment2 = nfa_stack.pop() 
            # Point fragment2 accept state at fragment1's start state
            fragment2.accept.edges.append(fragment1.start)
            # Create new instance of fragment to represent the new nfa
            newFragment = NFA_Fragments(fragment2.start, fragment1.accept)
            # Push new nfa to nfa stack
            nfa_stack.append(newFragment)
        elif c == '|':
            # Pop two fragments off the stack
            fragment1 = nfa_stack.pop()
            fragment2 = nfa.stack.pop()
            # Create new start and accept states
            accept = state(edges=[fragment2.start, fragment1.start])
            # Point the old accept states at the new one 
            fragment2.accept.edges.append(accept)
            fragment1.accept.edges.append(accept)
            # Create new instance of the fragment
            newFragment = NFA_Fragments(start, accept)
            # Push the new nfa to the stack
            nfa_stack.append(newFragment)
        elif c == '*':
            # Pop a single fragment off the stack
            NFA_Fragments = nfa_stack.pop()
            # Create new start and accept states
            accept = state()
            start = state(edges=[NFA_Fragments.start, accept])
            # Point the arrows 
            NFA_Fragments = accept.edges[NFA_Fragments.start, accept]
            # Create new instance of the fragment
            newFragment = NFA_Fragments(start, accept)
            # Push the new nfa to the stack
        else:
            accept = state()
            start = state(label=c, edges=[accept])
            # Create new instance of the fragment
            newNFA_Fragment = NFA_Fragments(start, accept)
        # Push the new nfa to the stack
        nfa_stack.append(newFragment)
    
    # The nfa stack should have exactly one nfa on it
    return nfa_stack.pop()

def match(regex, s):
    # Function will return true if the regular expression regex fully matches the string s, it returns false otherwise

    # Compile the regex into nfa 
    # Ask nfa if it matches the string s
    nfa = regex_compile(regex)
    return nfa

print (match ("a.b|b*", "bbbbbbbbbb"))



