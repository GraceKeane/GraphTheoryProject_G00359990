# Grace Keane
# Testing thompsons construction algorithm
# Running the result of the thompson.py 

# This python script can be used as a module so it can be
# imported on other python programs
# It matches infix regular expressions to strings

# Referance the script (thompson.py)
import thompson

# Pring to screen
print(thompson.match("a.b|b*", "bbbbbbbbbbbx"))
