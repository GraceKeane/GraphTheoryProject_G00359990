# ![Markdown Here logo](https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/Logo.png) 

## Contents
[Introduction](#introduction)<br>
[Run](#run)<br>
[Test](#test)<br>
[Algorithm](#algorithm)<br>
[Referances](#referances)
<br></br>

## Introduction
For this assignment I created a Python program that can build a non-deterministic finite automaton (NFA) from a regular expression. It then can use the NFA to check if the regular expression matches any hardcoded or prompted string of text. The program is based off an algorithm known as Thompson’s construction, named after the well-known computer scientist Ken Thompson

### Regular Expression (regex) <br>
The concept of regular expressions arose in the 1950s when the American mathematician Stephen Cole Kleene formalized the description of a regular language. A regular expression (shortened as regex or regexp, also referred to as rational expression) is a string containing a series of characters, some of which have a special meaning. They are commonly used in search engines and many programming languages provide regex capabilities either built-in or via libraries. Essentially regular expressions are used is a search pattern used for matching one or more characters within a string for this reason it is perfect for the implementation of this Graph Theory project. Some examples of regular expression operators are ? + | ^ . $ ( ) *
<br>

### Regular Expression operators <br>
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

### Non-deterministic finite automaton (NFA) <br>
NFAs were introduced in 1959 by Michael O. Rabin and Dana Scott. An NFA is a state machine that consists of numerous states that can accept or reject a finite string. Non-deterministic finite automata can have any number of arrows for each state and symbol.

*Sample NFA*
<p align="center">
  <img src="https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/Thompson's%20expressions%20%26%20descriptions/NFA.PNG" width="470" height="200">
</p>
The output of this NFA is 111101, 00001010, 1110
Explain how i got this result in basic stepts

## Run
How to run the program

## Test
How did i test the program

## Algorithm
Thompson construction was created by the famous computer scientist Ken Thompson. Thompson construction is a method of transforming a regular expression into an equivalent nondeterministic finite automaton. This NFA can be used to match strings against the regular expression. The algorithm works by splitting an expression into its corresponding subexpressions. 

### Rules for Thompson's construction
*Regular expression to NFA simple calculation*

<p align="center">
  <img src="https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/Thompson's%20expressions%20%26%20descriptions/Empty%20string.PNG" width="470" height="300">
</p>

## Referances
[Regular Expression - Wikipedia](https://en.wikipedia.org/wiki/Regular_expression) <br>
[Regular Expressions](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html) <br>
[Nondeterministic finite automaton](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton) <br>
[How to create a table of contents on git research](https://github.com/GraceKeane/github-markdown-toc) <br>
[Research on how to create a markdown image](https://github.com/GraceKeane/markdown-here)
[Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction)
