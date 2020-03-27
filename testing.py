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

print(thompson.match("a.b|b*", "bbbbbb"))

print(thompson.match("a.b|b*", "bbx"))

print(thompson.match("a.b", "ab"))

print(thompson.match("b**", "b"))

print(thompson.match("b*", ""))

print(thompson.match("A", "A"))

print(thompson.match("B","B"))

print(thompson.match("a.c|c*", "cccccc"))

print(thompson.match("c**", "c"))

print(thompson.match("a.b|c*", "dggfdert"))
