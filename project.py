# Grace Keane
# BSc in Computing in Software Development
# Graph theory project 2020
# Watched a brilliant video on how to implement this code,
# I added in comments to show what everything means/does
# Link https://www.youtube.com/watch?v=cD6qkvOYL_o&t=15s
# Steps described in documentation

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
            # * and / have the same value

            # if c is - or /
            if c in '-/':
                # - 1 from result
                result -= 1
            break

    return result

# ------------------------------------------------
# infix to postfix

# toPostfix recieves an expression
def toPostfix(expression):
    # Returnes another string
    result = ""

    # Stack holds 15 positions
    stack = Stack(15)

    # For each char in expression
    for char in expression:
        # Passing char to isOperand
        if isOperand(char):
            # Result is a string (point 1)
            result += char

        # Check if it is an operator, then pass a char
        # Stack is empty or has a left bracket on top -> push to stack (point 4)
        elif isOperator(char):
            while True:
                # Get the top char (not removing) (4i)
                topChar = stack.topChar()
                # If stack is empty or = to (
                if stack.isEmpty() or topChar == '(':
                    # Push char
                    stack.push(char)
                    # While takes break:
                    break

                # Labelling precedence hight -> low    +-*/^ (4ii)
                else:
                    # Precedence of char is equal to getPrecedence, then pass char
                    # Precedence = type of brackets
                    pC = getPrecedence(char)
                    # Precedence of the top char 
                    pTC = getPrecedence(topChar)
                    # If precedence of char is greater than the precedence of the top char  (4iii)  
                    if pC > pTC:
                        # Push on the stack if precedence is higher
                        stack.push(char)
                        # break because it is a while loop
                        break
                    else: #(4iii)
                        # If the precedence is lower or equal => pop, 
                        # print and repeat 4

                        # Because we have a while true we do not have to break
                        result += stack.pop()
        
        # If char is equal to left bracket (parenthesis)
        elif char == '(':
            # Left bracket -> push to the stack (point 2)
            stack.push(char)
        # If char is equal to right bracket (parenthesis) (point 3)
        elif char == ')':
            # Pop and print until left bracket if found
            # Then discard the left bracket

            # Get first char from the stack
            cpop = stack.pop()
            
            # Not equal to left bracket
            while cpop != '(':

                # Update the cpop 
                result += cpop
                # cpop is equal to stack.pop
                cpop = stack.pop()
    
    # While stack is not empty
    while not stack.isEmpty():
        cpop = stack.pop()
        result += cpop

    return result

# ---------------------------------------------------
# Result
# Calculates many at a time
infixExps1 = [
    #Infix      #Postfix 
    'A*B+C',    # AB*C+
    ]
infixExps2 = [
    'A+B*C',    # ABC*+
    ]
infixExps3 = [
    'A*B+C*D',  # AB*CD*+
    ]
infixExps4 = [
    'A*B^C+D',  # ABC^*D+
    ]
infixExps5 = [
    'A*(B+C*D)+E',          # ABCD*+*E+
    ]
infixExps6 = [
    'A+(B*C-(D/E^F)*G)*H',  # ABC*DEF^/G*-H*+
    ]
infixExps7 = [
    '(A+B)*C+D/(E+F*G)-H',  # AB+C*DEFG*+/+H-
    ]
infixExps8 = [
    'A-B-C*(D+E/F-G)-H'     # AB-CDEF/+G-*-H-
    ]

# Look over infix expression1
for exp in infixExps1:
    # Called postfix function
    postfix1 = toPostfix(exp)

# Look over infix expression2
for exp in infixExps2:
    # Called postfix function
    postfix2 = toPostfix(exp)

# Look over infix expression3
for exp in infixExps3:
    # Called postfix function
    postfix3 = toPostfix(exp)

# Look over infix expression4
for exp in infixExps4:
    # Called postfix function
    postfix4 = toPostfix(exp)

# Look over infix expression5
for exp in infixExps5:
    # Called postfix function
    postfix5 = toPostfix(exp)

# Look over infix expression6
for exp in infixExps6:
    # Called postfix function
    postfix6 = toPostfix(exp)

# Look over infix expression7
for exp in infixExps7:
    # Called postfix function
    postfix7 = toPostfix(exp)

# Look over infix expression8
for exp in infixExps8:
    # Called postfix function
    postfix8 = toPostfix(exp)


    # Print each result to screen
    print("Infix expression:" , infixExps1, "Result postfix expression", postfix1)
    print("Infix expression:", infixExps2, "Result postfix expression", postfix2)
    print("Infix expression:", infixExps3, "Result postfix expression", postfix3)
    print("Infix expression", infixExps4, "Result postfix expression", postfix4)
    print("Infix expression", infixExps5, "Result postfix expression", postfix5)
    print("Infix expression", infixExps6, "Result postfix expression", postfix6)
    print("Infix expression", infixExps7, "Result postfix expression", postfix7)
    print("Infix expression", infixExps8, "Result postfix expression", postfix8)


    







