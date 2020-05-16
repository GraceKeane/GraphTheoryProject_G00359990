# ![Markdown Here logo](https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/Logo.png) 

## Contents
* [Introduction](#introduction)<br>
  * [Program implementation stepts](#program-implementation-stepts)
  * [Important program files](#important-program-files)
  * [Regular Expression](#regular-expression)
  * [Regular Expression operators](#regular-expression-operators)
  * [Non-deterministic finite automaton](#non-deterministic-finite-automaton)
* [Run for Thompsons Construction](#run)<br>
* [Test](#test)<br>
* [Algorithm](#algorithm)<br>
* [Referances](#referances)
<br></br>

## Introduction
For this assignment I created a Python program that can build a non-deterministic finite automaton (NFA) from a regular expression. It then can use the NFA to check if the regular expression matches any hardcoded or prompted string of text. The program is based off an algorithm known as Thompson’s construction, named after the well-known computer scientist Ken Thompson.

### Program implementation stepts
*Easier to implement this program in steps rather than altogether*
1) Parse the regular expression from infix to postfix notation.
2) Build a series of small NFA’s for parts of the regular expression.
3) Use the smaller NFA’s to create the overall NFA.
4) Implement the matching algorithm using the NFA

## Important program files
1) "thompson.py" - The class thompson.py contains all the rules for this project to work. It stores important functions which are used to determine does a certain regular expression match a given string.
2) "testing.py" - This class used as a module so it can import thompson.py. It matches infix regular expressions to strings, the data in this class has been hardcoded.
3) "prompt.py" - I have developed a class that allows for user input. When a regular expression and a string is entered, the program then (by the help of the import keyword) follows the rules applied in "thompson.py" and detremines does the regular expression match the string specified.
4) "project.py" - I added an additional class called "project.py" that shows a differant way to parse a regular expression from infix to postfix. I followed a youtube video to do this. [Link](https://www.youtube.com/watch?v=cD6qkvOYL_o&t=15s)
5) "finaltesting.py" - This class contains more tests relating to regular expressions and strings it imports "thompson.py" to do so. It carries out numerous tests using the assert keyword to test every operator e.g. | . * + ?
6) "Help.py" - Allows users to learn how to use the program. Includes names of each class, class command and a brief description of classes in this programe.
7) "VSCREADME.txt" - I created a README using visual studio code.
8) "Thompson's expressions & descriptions" - Contains useful diagrams and edscriptions of regular expression operators.

### Regular Expression<br>
The concept of regular expressions arose in the 1950s when the American mathematician Stephen Cole Kleene formalized the description of a regular language. A regular expression (regex) is a string containing a series of characters, these special characters have a special meaning. They are mainly used in search engines and many programming languages provide regex capabilities either built-in or via libraries. Essentially regular expressions are used as a search pattern for matching one or more characters within a string, therefore for this reason they are perfect for the implementation of this Graph Theory project. Some examples of regular expression operators are ? + | ^ . $ ( ) *
<br>

### Regular Expression operators<br>
*Operators used in this Graph Theory project* <br>
( * ) - The Kleene star is represented as * . It matches the preceding element zero or more times. For example the regular expression ab*c matches "ac", "abc", "abbbc" ect but it does not match "abcd".

( + ) - The plus operator matches preceding elements one or more times. For example "ab+c" matches "abc", "abbc", "abbbc" and so on, but it does not match "ac".

( | ) - | is knows as the choice operator. It matches either the expression before or after the operator. For example "abc|def" matches either "abc" or "def"

( ? ) - This operator matches the preceding element zero or once. For example, "ab?c" matches only "ac" or "abc"

( . ) - The dot operator matches any single character. it matches a literal dot. For example, a.c matches "abc", etc, but "a.c" matches only "a", ".", or "c".

*Other regular expression operators* <br>
() - The opening and closed bracket defines a marked subexpression

( ^ ) - This regex operator matches the starting position of any line.

( [] ) - The opened and closed square brackets matches a single character that is located within the brackets e.g. "[abc]" matches characters "a", "b" or "c". Regex "[a-z]" matches any lowercase character from a to z.

( [^] ) - This specific operator matches a single character that is not contained within the square brackets. For example "[^def]" matches any characters other than "d", "e" or "f".

### Non-deterministic finite automaton<br>
NFAs were introduced in 1959 by Michael O. Rabin and Dana Scott. An NFA is a state machine that consists of numerous states that can accept or reject a finite string. Non-deterministic finite automata can have any number of arrows for each state and symbol.<br>
I have created diagrams converting imortant regex operator to their NFA forms [here](https://github.com/GraceKeane/GraphTheoryProject_G00359990/tree/master/Thompson's%20expressions%20%26%20descriptions)

*Sample beginner regex to NFA calculations*
<b> Converting X|YZ to NFA format </b>

<p align="center">
  <img src="https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/Thompson's%20expressions%20%26%20descriptions/NFA.PNG" width="470" height="200">
</p>


## Run
How to run the program

## Test
How did i test the program

## Algorithm
Thompson construction was created by the famous computer scientist Ken Thompson. Thompson construction is a method of transforming a regular expression into an equivalent nondeterministic finite automaton. This NFA can be used to match strings against the regular expression. The algorithm works by splitting an expression into its corresponding subexpressions. 

### Rules for Thompson's construction
*Regular expression to NFA simple calculation*



## Referances
* Showed me the various regular expressions and functions - [Regular Expressions](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html) 
* How to create a table of contents on git research - [Table of contents on git](https://github.com/GraceKeane/github-markdown-toc)
* Research on how to create a markdown image -[Markdown image](https://github.com/GraceKeane/markdown-here)
* Additional ways of implementing infix to postfix in python - [Infix to postfix in python](https://www.youtube.com/watch?v=cD6qkvOYL_o&t=15s)
* Describing what a regular expression is essentially - [Regular language](https://en.wikipedia.org/wiki/Regular_language)
* Research of what Thompson's construction consists of - [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction)
* Describing what an NFA is essentially - [Nondeterministic finite automaton](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)
* How to implementing a regular expression engine - [Implementing a Regular Expression Engine](https://deniskyashif.com/2019/02/17/implementing-a-regular-expression-engine/)
* Infix to postfix algorithm - [Infix to postfix - algorithm and exercises](https://www.youtube.com/watch?v=yTpzVWO1Dis)
* Stack, infix and postfix research - [Stack | set 2 (infix to postfix)](https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/) 
* Research of what the Kleene star is essentially - [Kleene star](https://en.wikipedia.org/wiki/Kleene_star)
* What a Unary operation is essentially - [Unary operation](https://en.wikipedia.org/wiki/Unary_operation)
* More research on regular expressions - [Regular expressions](https://en.wikipedia.org/wiki/Regular_expression)
* VScode readME research - [Using Git with VS Code and Github](https://www.youtube.com/watch?v=9cMWR-EGFuY)
* More VSCode readME research - [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)
* Research on how to use titles as links - [Getting Started With GitHub, Part 3: Creating a Read Me File in Markdown](https://www.youtube.com/watch?v=yXY3f9jw7fg)
