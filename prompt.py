# Grace Keane - G00359990
# Graph Theory project 2020
# User input class

"""This class imports the main class thompson.py 
and allows the user to enter a regular expression 
and a string, it then determines do they match
by following the rules applied in thompson.py.
"""

import thompson

# Taking input in - https://stackoverflow.com/a/15190742
# Printing out the data given - https://www.geeksforgeeks.org/taking-input-in-python/

## Variables
# s = String
# regex = Regular expression

regex = raw_input("Please enter a regular expression: ")
print (regex)
s = raw_input("Please enter a string to match: ")
print (s)

while s != "q":
    if (thompson.match(regex, s)):
        print(regex, " matches the string: ", s)
    else:
        print(regex, " does not match the string: ", s)

    # Continue - prompt the user for information (regular expression & string)
    regex = raw_input("\n(q - quit) Please enter a regular expression to match: ")
    print (regex)
    s = raw_input("\n(q - quit) Please enter a string to match: ")
    print (s)
