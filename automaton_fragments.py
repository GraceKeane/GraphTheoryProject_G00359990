# Grace Keane
# Graph theory
# Software Development
# Automaton fragments using Python & Thompsons algorithm

class State:
    # Every state has 0, 1 or 2 edges from it
    edges = []

    # Label for the arrows. None means epsilon
    label = None 

    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label

class Fragment:
    # Start state of NFA fragment
    start = None
    # Accept state of NFA fragment
    accept = None

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def shunt(infix):
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
        c = infix.pop() # Removes the last element in infix as a list & returns whatever is poped off

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
            # Push c to the operator stack
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
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        # Pop a character from postfix
        c = postfix.pop()
        if c == '.':
            # Pop two fragments off the stack
            frag1 = nfa_stack.pop()   
            frag2 = nfa_stack.pop()
            # Point frag2 accept state at frag1 start state
            frag2.accept.edges.append(frag1.start)
            # Create new instance of Fragment to represent the new NFA
            newfrag = Fragment(frag2.start, frag1.accept)
            # Push the new NFA to the NFA stack
            nfa_stack.append(newfrag)
        elif c == '|':
            # Pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Create new start and accept states
            accept = State()
            start = State (edges=[frag2.start, frag1.start])
            # Point the old accept state at the new accept state
            frag1.accept.edges.append(accept)
            frag2.accept.edges.append(accept)
            # Create new instance of the fragment
            newfrag = Fragment(start, accept)
            nfa_stack.append(newfrag)
        elif c == '*':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()
            accept = State()
            start = State(edges=[frag.start, accept])
            # Point the arrows
            frag.accept.edge = ([frag.start, accept])
            # Create new instance of the fragment
            newfrag = Fragment(start, accept)
        else:
            accept = State()
            initial = State(label=c, edges=[accept])
            # Create new instance of the fragment
            newfrag = Fragment(initial, accept)
        # Push new nfa to the stack
        nfa_stack.append(newfrag)

    # The NFA stack should have exactly one NFA on it
    return nfa_stack.pop()


def match(regex, s):
    # This function will return true if the regular expression
    # regex fully matches the string s. It returns false otherwise

    # Compile the regular expression into an NFA
    nfa = regex_compile(regex)
    # Ask the NFA if it matches the string s
    return nfa

print(match("a.b|b*", "bbbbbbbbbb"))

