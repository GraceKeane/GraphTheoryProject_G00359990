# ![Markdown Here logo](https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/Logo.png) 

## Contents
[Introduction](#introduction)<br>
[Run](#run)<br>
[Test](#test)<br>
[Algorithm](#algorithm)<br>
[Referances](#referances)
<br></br>

## Introduction
For this assignment I created a Python program that can build a non-deterministic finite automaton (NFA) from a regular expression. It then can use the NFA to check if the regular expression matches any hardcoded or prompted string of text. 

<b>Regular Expression (regex)</b><br>
The concept of regular expressions arose in the 1950s when the American mathematician Stephen Cole Kleene formalized the description of a regular language. A regular expression (shortened as regex or regexp, also referred to as rational expression) is a string containing a series of characters, some of which have a special meaning. They are commonly used in search engines and many programming languages provide regex capabilities either built-in or via libraries. Essentially regular expressions are used is a search pattern used for matching one or more characters within a string for this reason it is perfect for the implementation of this Graph Theory project. Some examples of regular expression operators are ? + | ^ . $ ( ) *
<br>

<b>Regular Expression operators</b> <br>
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

<b>Non-deterministic finite automaton (NFA)</b><br>
NFAs were introduced in 1959 by Michael O. Rabin and Dana Scott. An NFA is a state machine that consists of numerous states that can accept or reject a finite string. Non-deterministic finite automata can have any number of arrows for each state and symbol.

## Run

## Test

## Algorithm

## Referances
[Regular Expression - Wikipedia](https://en.wikipedia.org/wiki/Regular_expression) <br>
[Regular Expressions](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html) <br>
[Nondeterministic finite automaton](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)
