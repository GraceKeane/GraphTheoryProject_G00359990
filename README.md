## Graph Theory project
### Grace Keane
### ID - G00359990

Thompsons construction is a method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA). NFAs can be used to match strings against the regular expression. NFA is short for non-deterministic finite automaton, It was designed and implemented by Michael O. Rabin and Dana Scott. NFA’s were designed and implemented to only recognise regular languages.

A regular expression (also called regex) is a string containing a series of characters that have special meaning. For example, the three characters |, .  and * have the special meanings of concatenate, or, and Kleene star. The regular expression 0.1 means a 0 followed by a 1, 0|1 means a 0 or a 1, and 1* means any number of 1’s. More regular expression examples are defined in [overview.md](https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/overview.md) file. For this project I implemented the * | . ? + operators.

Non-deterministic finite automatons (NFA) were introduced in 1959 by Michael O. Rabin and Dana Scott. An NFA is a state machine that consists of numerous states that can accept or reject a finite string. An NFA can have any number of arrows for each state and symbol.<br>

I have created diagrams converting important regular expressions (regex) operator to their Non-deterministic finite automaton (NFA) forms [here](https://github.com/GraceKeane/GraphTheoryProject_G00359990/tree/master/Thompson's%20expressions%20%26%20descriptions)

I also have done a basic calculation to demonstrate converting a regular expression (regex) to a Non-deterministic finite automaton (NFA) in my [overview.md](https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/overview.md) file.

Python has well-defined rules for specifying the order in which the operators in an expression are evaluated when the expression has several operators. For example, multiplication and division have a higher precedence than addition and subtraction. Precedence rules can be overridden by explicit parentheses.

*Order of precedence levels*
1) ( * )
2) ( . )
2) ( + )
3) ( | )
4) ( ? )

The Thompsons construction algorithm works by splitting an expression into its constituent subexpressions. This algorithm is created by a computer scientist called Kem Thompson.

*More information is available in my [overview.md](https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/overview.md) file*

For this project I am instructed to implement Thompson’s construction algorithm to determine does a given regular expression match the string assigned.

## Architecture
1) <b>thompson.py</b> - The class thompson.py contains all the rules for this project to work. It stores important functions which are used to determine does a certain regular expression match a given string.
2) <b>testing.py</b> - This class used as a module so it can import thompson.py. It matches infix regular expressions to strings, the data in this class has been hardcoded.
3) <b>prompt.py</b> - I have developed a class that allows for user input. When a regular expression and a string is entered, the program then (by the help of the import keyword) follows the rules applied in "thompson.py" and determines does the regular expression match the string specified.
4) <b>project.py</b> - I added an additional class called "project.py" that shows a different way to parse a regular expression from infix to postfix. I followed a YouTube video to do this. [Link](https://www.youtube.com/watch?v=cD6qkvOYL_o&t=15s)
5) <b>finaltesting.py</b> - This class contains more tests relating to regular expressions and strings it imports "thompson.py" to do so. It carries out numerous tests using the assert keyword to test every operator e.g. | . * + ?
6) <b>Help.py</b> - Allows users to learn how to use the program. Includes names of each class, command to use the class and a brief description of what each class does.
7) <b>VSCREADME.txt</b> - I created a README using visual studio code.
8) <b>Thompson's expressions & descriptions</b> - Contains useful diagrams and descriptions of regular expression operators. I created most of these diagrams myself with the use of Microsoft paint.

## References
* Describing what an NFA is essentially - [Nondeterministic finite automaton](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)
* How to implementing a regular expression engine - [Implementing a Regular Expression Engine](https://deniskyashif.com/2019/02/17/implementing-a-regular-expression-engine/)
* Infix to postfix algorithm - [Infix to postfix - algorithm and exercises](https://www.youtube.com/watch?v=yTpzVWO1Dis)
* Stack, infix and postfix research - [Stack | set 2 (infix to postfix)](https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/) 
* Research of what the Kleene star is essentially - [Kleene star](https://en.wikipedia.org/wiki/Kleene_star)
* What a Unary operation is essentially - [Unary operation](https://en.wikipedia.org/wiki/Unary_operation)
* More research on regular expressions - [Regular expressions](https://en.wikipedia.org/wiki/Regular_expression)
* VScode readME research - [Using Git with VS Code and GitHub](https://www.youtube.com/watch?v=9cMWR-EGFuY)
* More VSCode readME research - [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)
* Research on how to use titles as links - [Getting Started With GitHub, Part 3: Creating a Read Me File in Markdown](https://www.youtube.com/watch?v=yXY3f9jw7fg)
* Additional ways of implementing infix to postfix in python - [Infix to postfix in python](https://www.youtube.com/watch?v=cD6qkvOYL_o&t=15s)
* Describing what a regular expression is essentially - [Regular language](https://en.wikipedia.org/wiki/Regular_language)
* Research of what Thompson's construction consists of - [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction)
* Showed me the various regular expressions and functions - [Regular Expressions](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html) 
* Shows the hierarchy of regex precedence - [C Operator Precedence](https://en.cppreference.com/w/c/language/operator_precedence)
* Simple example of getting raw input from a user in prompt class - [raw_input function in Python](https://stackoverflow.com/a/5563119/13407257)
* Showed me differant examples of how to use the assert keyword when testing in finaltesting.py - [Assert - Chai](https://www.chaijs.com/api/assert/)

## Technologies used
* Google cloud SSH engine
* Python V 3.7
