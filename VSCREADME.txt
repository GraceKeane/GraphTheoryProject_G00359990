# GraphTheoryProject_G00359990 - Grace Keane

Thompsons construction is a method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA). NFAs can be used to match strings against the regular expression. NFA is short for non-deterministic finite automaton, It was designed and implemented by Michael O. Rabin and Dana Scott. NFA’s are designed to only recognise regular languages.

A regular expression is a string containing a series of characters that have special meaning. For example, the three characters |, .  and * have the special meanings concatenate, or, and Kleene star. For example, the regular expression 0.1 means a 0 followed by a 1, 0|1 means a 0 or a 1, and 1* means any number of 1’s. More regular expression examples are Plus, times, start, or, kleene star, question, end.

Python has well-defined rules for specifying the order in which the operators in an expression are evaluated when the expression has several operators. For example, multiplication and division have a higher precedence than addition and subtraction. Precedence rules can be overridden by explicit parentheses.

The Thompsons construction algorithm works by splitting an expression into its constituent subexpressions. This algorithm is created by a computer scientist called Kem Thompson.

For this project I am instructed to implement thompson's construction algorithm to determine does a given regular expression match the string assigned.

## Architecture
* "thompson.py" - The class thompson.py contains all the rules for this project to work. It stores important functions which are used to determine does a certain regular expression match a given string. 
* "testing.py" - This class used as a module so it can import thompson.py. It matches infix regular expressions to strings, the data in this class has been hardcoded in. 
* "prompt.py" - I have developed a class that allows for user input. When a  regular expression and a string is entered, the program then (by the help of the import keyword) follows the rules applied in "thompson.py" and detremines does the regular expression match the string specified. 
* "project.py" - I added an additional class called "project.py" that shows a differant way to parse a regular expression from infix to postfix. I followed a youtube video to do this. [Link](https://www.youtube.com/watch?v=cD6qkvOYL_o&t=15s)
* "finaltesting.py" - This class contains more tests relating to regular expressions and strings it imports "thompson.py" to do so. It carries out numerous tests using the assert keyword to test every operator e.g. | . * + ?
* "VSCREADME.txt" - I created a README using visual studio code

## What I learned 
* The syntax for regular expressions
* How a regex engine works
* How to understand the internals of the Google Cloud SSH engine
* How to break a complex problem into smaller problems
* Different ways of thinking about the problem
* Differance between regular expressions
* How to create a README using Visual studio code
* How to create and merge braches in GitHub

## Research links
* Additional ways of implementing infix to postfix in python - [Infix to postfix in python](https://www.youtube.com/watch?v=cD6qkvOYL_o&t=15s)
* Describing what a regular expression is essentially - [Regular language](https://en.wikipedia.org/wiki/Regular_language)
* Research of what Thompson's construction consists of - [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction)
* Describing what an NFA is essentially - [Nondeterministic finite automaton](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)
* How to implementing a regular expression engine - [Implementing a Regular Expression Engine](https://deniskyashif.com/2019/02/17/implementing-a-regular-expression-engine/)
* Infix to postfix algorithm - [Infix to postfix - algorithm and exercises](https://www.youtube.com/watch?v=yTpzVWO1Dis)
* Stack, infix and postfix research - [Stack | set 2 (infix to postfix)](https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/) 
* Research of what the Kleene star is essentially - [Kleene star](https://en.wikipedia.org/wiki/Kleene_star)
* What a Unary operation is essentially - [Unary operation](https://en.wikipedia.org/wiki/Unary_operation)
* More research on regylar expressions - [Regular expressions](https://en.wikipedia.org/wiki/Regular_expression)
* VScode readME research - [Using Git with VS Code and Github](https://www.youtube.com/watch?v=9cMWR-EGFuY)
* More VSCode readME research - [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)
* Research on how to use titles as links - [Getting Started With GitHub, Part 3: Creating a Read Me File in Markdown](https://www.youtube.com/watch?v=yXY3f9jw7fg)

## Problems faced & overcome
I had problems submitting my code to git. Usually when I committed my code it published numerous files to my GitHub repository that I did not need. I then had to delete them all again. I researched ways on how to commit my code correctly using git and I found this video helped me a lot. It showed me how to commit the changes that I needed to GitHub with the use of branches and then merging to the master branch.   

1.	Git branch myBranchName (Creating a new branch)
2.	Git branch (Displaying all branches created)
3.	Git checkout myBranchName (Switches to the new branch created)
4.	Git add .
5.	Git commit -m “Comments go here”
6.	Git push --set-upstream origin branch1
7.	Enter username
8.	Enter password
9.	Go to your repository on [GitHub](www.github.com)
10.	Click “Compare & pull request”
11.	Click “Create pull request”
12.	Click “Merge pull request”
13.	Click “Confirm merge”

[Research link](https://www.youtube.com/watch?v=JTE2Fn_sCZs)


## Class videos implemented
### I implemented the code from the videos separately so that I can see how the application can be broken up into smaller parts

Introduction to Python => https://github.com/GraceKeane/GraphTheory


Automaton fragments => https://github.com/GraceKeane/Automaton-fragments                                                                    

Shunting yard algorithm => https://github.com/GraceKeane/Shunting-yard-algorithm                                                                

Using Python => https://github.com/GraceKeane/Python                                                                                              

Matching a regular expression with a string => https://github.com/GraceKeane/Python-Matching

Classes for Thompson => https://github.com/GraceKeane/Classes-for-Thompsons-algorithm


Cleaning & testing => https://github.com/GraceKeane/Cleaning-Testing

## Technologies used
* Google cloud SSH engine
* Python V 3.7
