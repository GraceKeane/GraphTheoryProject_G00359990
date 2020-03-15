# Grace Keane
# BSc in Computing in Software Development
# Graph theory project 2020

# My stack class
# Implementing the stack
class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)

    def pop(self):
        result = -1

        if self.stack != []:
            result = self.stack.pop()

        return result

    def display(self):
        if self.stack == []:
            print("Stack is empty!")
        else:
            print("Stack data:")
            for item in reversed(self.stack):
                print(item)

    def isEmpty(self):
        return self.stack == []

    def topChar(self):
        result = -1

        if self.stack != []:
            result = self.stack[len(self.stack) - 1]

        return result

# ----------------------------------------------
# Operations

# Operand
# If it is an operand it will check if it is an
# upper case char from A - Z
def isOperand(c):
    return c >= 'A' and c <= 'Z'

# Plus, minus, times, divide, power off
operators = "+-*/^"

# Operator
# Operator checks if the given char is one of these => + - * / ^
def isOperator(c):
    return c in operators

# Precedence

# Recieves a char
def getPrecedence(c):
    # Result is an integer
    result = 0
    
    # Iterates over the operator string
    for char in operators:
        # For each iteration it will increase the number of result
        result += 1

        # if char is equal to the given char 
        if char == c:
            # If char is equal to minus or division it will decrease
            # one from the result and then break 
            # Because minus and division have the same value
            if c in '-/':
                result -= 1
            break

    return result

# ------------------------------------------------
# infix to postfix
def toPostfix(expression):
    # Returnes another string
    result = ""

    stack = Stack(15)

    for char in expression:
        if isOperand(char):
            # Result is a string
            result += char

        # Check if it is an operator, then pass a char
        # Stack is empty or has a left bracket on top -> push to stack
        elif isOperator(char):
            while True:
                # Get the top char (not removing)
                topChar = stack.topChar()
                
                if stack.isEmpty() or topChar == '(':
                    # Push char
                    stack.push(char)
                    # While takes break:
                    break
                else:
                    # Precedence of char is equal to getPrecedence, then pass char
                    # Precedence = type of brackets
                    pC = getPrecedence(char)
                    # Precedence of the top char 
                    pTC = getPrecedence(topChar)
                    # If precedence of char is greater than the precedence of the top char    
                    if pC > pTC:
                        # Push on the stack if precedence is higher
                        stack.push(char)
                        # break because it is a while loop
                        break
                    else:
                        # If the precedence is lower or equal => pop, 
                        # print and repeat 4

                        # Because we have a while true we do not have to break
                        result += stack.pop()
        
        # If char is equal to left bracket
        elif char == '(':
            # Left bracket -> push to the stack
            stack.push(char)
        # If char is equal to right bracket
        elif char == ')':
            # Pop and print until left bracket if found
            # Then discard the left bracket

            # Get first char from the stack
            cpop = stack.pop()
            
            # Not equal to left bracket
            while cpop != '(':

                # Update the cpop 
                result += cpop
                cpop = stack.pop()
    
    while not stack.isEmpty():
        cpop = stack.pop()
        result += cpop

    return result

# ---------------------------------------------------
# Result
infixExps = [
    #Infix      #Postfix 
    'A*B+C',    # AB*C+
    'A+B*C',    # ABC*+
    'A*B+C*D',  # AB*CD*+
    'A*B^C+D',  # ABC^*D+
    'A*(B+C*D)+E',          # ABCD*+*E+
    'A+(B*C-(D/E^F)*G)*H',  # ABC*DEF^/G*-H*+
    '(A+B)*C+D/(E+F*G)-H',  # AB+C*DEFG*+/+H-
    'A-B-C*(D+E/F-G)-H'     # AB-CDEF/+G-*-H-
]
# Look over infix expressions
for exp in infixExps:
    # Called postfix function
    postfix = toPostfix(exp)
    
    # Print the result
    print("-----Infix-----")
    print(infixExps)
    print("-----Postfix-----")
    print(postfix)

