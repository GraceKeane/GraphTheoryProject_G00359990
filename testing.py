# Grace Keane
# Testing thompson's construction algorithm
# Running the result of the thompson.py 

"""This python script can be used as a module so it can be
imported on other python programs. It matches infix regular
expressions to strings.
"""

#Import & referance the script (thompson.py)
import thompson

# Checking does the regular expression match the string
# Print to screen
print(thompson.match("a.b|b*", "bbbbbbbbbbbx"))
