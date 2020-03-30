# Grace Keane - G00359990
# Graph Theory project 2020

"""This class imports the main class thompson.py 
and allows the user to 
"""

import thompson

# Taking input in python - https://www.geeksforgeeks.org/taking-input-in-python/

regexpression = input("Please enter a regular expression: ")
stringMatch = input("Please enter a string to match: ")

while stringMatch != "q":
    if (project.match(regexpression, stringMatch)):
        print(regexpression, "matches the string: ", stringMatch)
    else:
        print(regexpression, "does not match the string: ", stringMatch)
    stringMatch = input("\n(q - quit) Please enter a string to match: ")
