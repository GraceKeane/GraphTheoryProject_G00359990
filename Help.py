# Importing argparse
import argparse

# Allows for input
s = raw_input("Please enter --help for help or q to quit ")

# If --help is entered it prints out data to help user
if s == "--help":

    # Class names, how to run class and added description

    print("\nThompson | Run class - thompson.py")
    print("thompson.py holds all rules to determine if a regular expression matches a given string")
    
    print("\nTesting | Run class - testing.py")
    print("Imports thompson.py module to determing does hardcoded data match infix regex to strings")

    print("\nPrompt | Run class - prompth.py")
    print("Allows for user input, detremines does the regular expression match the string specified")

    print("\nProject | Run class - project.py")
    print("Demonstrates a different method to parse a regular expression from infix to postfix")

    print("\nFinal testing | Run class = finaltesting.py")
    print("Tests relating to regex and strings, uses the assert keyword to test operators(| . * + ?)\n")

# If q is ented, program quits
elif s == "q":
    s = raw_input("\n(q - quit) Are you sure you want to quit: ")





