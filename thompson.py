# Grace Keane - G00359990
# Graph Theory project 2020
# BSc in Computing in Software Development
# Thompsons construction algorithm using python
# Python 3.7

# Main project class 
# finaltesting.py tests this class

class State:
    # Doc string comment - Comments multiple lines at once.
    """State function -> returnes a state with one or
    two edges , all edges labelled by label
    """

    # Constructor
    def __init__(self, label=None, edges=[]):
        # Every state has 0, 1, or 2 edges from it
        self.edges = edges
        # Label for the arrows. None means epsilon
        self.label = label

class Fragment:
    """Fragment function -> returnes an NFA fragment
    with a start state and an accept state
    """

    # Constructor
    def __init__(self, start, accept):
        # Start state of NFA fragment
        self.start = start
        # Accept state of NFA fragment
        self.accept = accept

def shunt(infix):
    # Doc string - string inside class/ function
    """Shunt function -> returnes the infix regular
    expression to postfix
    """

    infix = list(infix)[::-1]

    # Operator stack
    opers = []
     
    # Postfix regular expression
    postfix = []

    # Operator precidence * - . - |
    prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

    # Loop through the input, one character at a time
    while infix:
        # Pop a character from the list
        c = infix.pop() # Removes the last element in infix as a list
                        # & returns whatever is poped off

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


def compile(infix):
    """Compile function -> returnes an NFA fragment
    representing the infix regular expression
    """

    # Convert infix to postfix
    postfix = shunt(infix)
    # Make postfix a stack of characters
    postfix = list(postfix)[::-1]

    # Stack for NFA fragments
    nfa_stack = []

    while postfix:
        # Pop a character from postfix
        c = postfix.pop()
        # Concatenate operator - Matches any single character
        if c == '.':
            # Pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Point frag2 accept state at frag1 start state
            frag2.accept.edges.append(frag1.start)
            # The new start state is frag2's
            start = frag2.start
            # The new accept state is frag1's
            accept = frag1.accept
        # Or operator -  expression before or the expression after
        elif c == '|':  
            # Pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Create new start and accept states
            accept = State()
            start = State (edges=[frag2.start, frag1.start])
            # Point the old accept state at the new accept state
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
        # Kleene star operator - Zero or more
        elif c == '*':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()
            accept = State()
            start = State(edges=[frag.start, accept])
            # Point the arrows
            frag.accept.edges = [frag.start, accept]
        # Plus operator - One or more
        elif c == '+':
            # Pop the last fragment off the stack
            frag = nfa_stack.pop()
            # Create a new accept state
            accept = State()
            # Create a new start state
            start = State(edges=[frag.start])
            # Point at the start state
            frag.accept.edges.append(frag.start)
            # Point the old accept state at the new accept state
            frag.accept.edges.append(accept)
        # Question operator - Zero or one
        elif c == '?':
            # Pop the last fragment off the stack
            frag = nfa_stack.pop()
            # Create a new accept state
            accept = State()
            # Pop a single fragment off the stack
            start = State(edges=[frag.start, accept])
            # Point to accept state
            frag.start.edges.append(frag.accept)
            # Point the old accept state at the new accept state
            frag.accept.edges.append(accept)
        
        else:
            accept = State()
            start = State(label=c, edges=[accept])

        # Create new instance of Fragment to represent the new NFA 
        newfrag = Fragment(start, accept)
        # Push new nfa to the stack
        nfa_stack.append(newfrag)

    # The NFA stack should have exactly one NFA on it
    return nfa_stack.pop()

def followes(state, current):
    """Followes function -> adds a state to a set and then
    follows all of the e(psilon) arrows
    """

    # Only do something when haven't already seen the state
    if state not in current:
    # Put the state itself into current
        current.add(state)
        # See whether state is labeled by e(epsilon)
        # Epsilon = empty string
        if state.label is None:
            # Loop through the states pointed by this state
            for x in state.edges:
                # Follow all of their epsilons too
                followes(x, current)

def match(regex, s):
    """Match function -> this  function will return true
    if the regular expression, regex fully matches the string s.
    It returns false otherwise
    """

    # Compile the regular expression into an NFA
    nfa = compile(regex)
    
    # Try to match the regular expression to the string s
    # The current set of states
    current = set()
    # Add the first state and follow all epsilon arrows
    followes(nfa.start, current)
    # The previous set of states
    previous = set()

    # Loop through characters in s
    for c in s:
        # Keep track of where you were
        previous = current
        # Create a new empty set for the states we're about to be in
        current = set()
        # Loop through the previous states
        for state in previous:
            # Only follow arrows not labeled e(epsilon) 
            if state.label is not None:
                # If the label of the state is equal to the character we've read
                if state.label == c:
                    # Add the state at the end of the arrow to current
                    followes(state.edges[0], current)
                    
    # Ask the NFA if it matches the string s
    return nfa.accept in current

