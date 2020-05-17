# ![Markdown Here logo](https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/Logo.png) 

## Contents
* [Introduction](#introduction)<br>
  * [Program implementation stepts](#program-implementation-stepts)
  * [Important program files](#important-program-files)
* [Algorithm](#algorithm)<br>
  * [Infix and Postfix notations](#infix-and-postfix-notations)
  * [Regular Expression](#regular-expression)
  * [Regular Expression operators](#regular-expression-operators)
  * [Non-deterministic finite automaton](#non-deterministic-finite-automaton)
  * [Beginner calculations](#Beginner-calculations)
* [Run](#run)<br>
  * [Various downloads needed](various-downloads-needed)
  * [Commands to run your code](commands-to-run-your-code)
* [Test](#test)<br>
* [Referances](#referances)
<br></br>

## Introduction
For this assignment I created a Python program that can build a non-deterministic finite automaton (NFA) from a regular expression. It then can use the NFA to check if the regular expression matches any hardcoded or prompted string of text. The program is based off an algorithm known as Thompson’s construction, named after the well-known computer scientist Ken Thompson.

### Program implementation stepts
*Easier to implement this program in steps rather than altogether*
1) Parse the regular expression from infix to postfix notation.
2) Build a series of small NFA’s for parts of the regular expression.
3) Use the smaller NFA’s to create the overall NFA.
4) Implement the matching algorithm using the NFA.

### Important program files
1) <b>thompson.py</b> - The class thompson.py contains all the rules for this project to work. It stores important functions which are used to determine does a certain regular expression match a given string.
2) <b>testing.py</b> - This class used as a module so it can import thompson.py. It matches infix regular expressions to strings, the data in this class has been hardcoded.
3) <b>prompt.py</b> - I have developed a class that allows for user input. When a regular expression and a string is entered, the program then (by the help of the import keyword) follows the rules applied in "thompson.py" and detremines does the regular expression match the string specified.
4) <b>project.py</b> - I added an additional class called "project.py" that shows a differant way to parse a regular expression from infix to postfix. I followed a youtube video to do this. [Link](https://www.youtube.com/watch?v=cD6qkvOYL_o&t=15s)
5) <b>finaltesting.py</b> - This class contains more tests relating to regular expressions and strings it imports "thompson.py" to do so. It carries out numerous tests using the assert keyword to test every operator e.g. | . * + ?
6) <b>Help.py</b> - Allows users to learn how to use the program. Includes names of each class, command to use the class and a brief description of of what each class does.
7) <b>VSCREADME.txt</b> - I created a README using visual studio code.
8) <b>Thompson's expressions & descriptions</b> - Contains useful diagrams and descriptions of regular expression operators. I created most of these diagrams myself with the use of microsoft paint.

## Algorithm
Thompson construction was created by the famous computer scientist Ken Thompson. Thompson construction is a method of transforming a regular expression into an equivalent nondeterministic finite automaton. This NFA can be used to match strings against the regular expression. The algorithm works by splitting an expression into its corresponding subexpressions. 

### Infix and Postfix notations
Infix: For example - a operand b. When an operator is in-between every pair of operands. 
Postfix:For example - a b operand. When an operator is followed by every pair of operands.

These operators forms mathematical expressions using parentheses. I have described the various precidence levels and rules in readMe.md.

An example of infix notation would be A * B + C / D. If I converted that equation to postfix it would follow the rules of precidence and the output would be + * A B/ C D.

### Regular Expression<br>
The concept of regular expressions arose in the 1950s when the American mathematician Stephen Cole Kleene formalized the description of a regular language. A regular expression (also called regex) is a string containing a series of characters, these special characters have a special meaning. They are mainly used in search engines and many programming languages provide regex capabilities either built-in or with the use of libraries. Essentially regular expressions are used as a search pattern for matching one or more characters within a string, therefore for this reason they are perfect for the implementation of this Graph Theory project. Some examples of regular expression operators are ? + | ^ . $ ( ) *
<br>

### Regular Expression operators<br>
*Operators used in this Graph Theory project* <br>
( * ) - The Kleene star is represented as * . It matches the preceding element zero or more times. For example the regular expression ab*c matches "ac", "abc", "abbbc" ect but it does not match "abcd".

( + ) - The plus operator matches preceding elements one or more times. For example "ab+c" matches "abc", "abbc", "abbbc" and so on, but it does not match "ac".

( | ) - | is knows as the choice operator. It matches either the expression before or after the operator. For example "abc|def" matches either "abc" or "def" but would not match "hij", "abf" ect.

( ? ) - This operator matches the preceding element zero or once. For example, "ab?c" matches only "ac" or "abc".

( . ) - The dot operator matches any single character. For example, a.c matches "abc", etc, but "a.c" matches only "a", ".", or "c".

*Other regular expression operators* <br>
() - The opening and closed bracket defines a marked subexpression.

( ^ ) - This regex operator matches the starting position of any line.

( [] ) - The opened and closed square brackets matches a single character that is located within the brackets. For example  "[abc]" matches characters "a", "b" or "c". Regex "[a-z]" matches any lowercase character from a to z.

( [^] ) - This specific operator matches a single character that is not contained within the square brackets. For example   "[^def]" matches any characters other than "d", "e" or "f".

### Non-deterministic finite automaton<br>
NFAs were introduced in 1959 by Michael O. Rabin and Dana Scott. An NFA is a state machine that consists of numerous states that can accept or reject a finite string. Non-deterministic finite automata can have any number of arrows for each state and symbol.<br>
I have created diagrams converting imortant regex operator to their NFA forms [here](https://github.com/GraceKeane/GraphTheoryProject_G00359990/tree/master/Thompson's%20expressions%20%26%20descriptions)

### Beginner calculations<br>
<b> Converting X|YZ to NFA format </b> <br>
For this equation i broke the regex up into smaller parts. Diagram 1 demonstrates the Or operators functionality between "X" and "YZ". The Or operator in this case has two transitions between them. Diagram 2 demonstrates breaking down the "YZ" into its constituent components. YZ has an intermediate state. The circle on the left is called the begining state and the right circle is called the accept state. I created and designed these diagrams myself using the microsoft paint application on my PC <br>

<p align="center">
  <img src="https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/Thompson's%20expressions%20%26%20descriptions/cal1.PNG" width="250" height="250">
</p>
<b>Diagram 1</b>

<p align="center">
  <img src="https://github.com/GraceKeane/GraphTheoryProject_G00359990/blob/master/Thompson's%20expressions%20%26%20descriptions/cal2.PNG" width="250" height="250">
</p>
<b>Diagram 2</b> 

## Run
### Various downloads needed
In order to create this project yourself various accounts must be created and some libraries must be downloaded.
1) <b>[Google cloud account](https://accounts.google.com/ServiceLogin/signinchooser?service=cloudconsole&passive=1209600&osid=1&continue=https%3A%2F%2Fconsole.cloud.google.com%2Fgetting-started%3Fproject%3Ddirected-smoke-265423%26pli%3D1%26login%3Dtrue%26ref%3Dhttps%3A%2F%2Faccounts.google.com%2FLogout%3Fservice%253Dcloudconsole%2526continue%253Dhttps%3A%2F%2Fconsole.cloud.google.com%2Fgetting-started%3Fproject%25253Ddirected-smoke-265423%252526pli%25253D1%2526hl%253Den_US&followup=https%3A%2F%2Fconsole.cloud.google.com%2Fgetting-started%3Fproject%3Ddirected-smoke-265423%26pli%3D1%26login%3Dtrue%26ref%3Dhttps%3A%2F%2Faccounts.google.com%2FLogout%3Fservice%253Dcloudconsole%2526continue%253Dhttps%3A%2F%2Fconsole.cloud.google.com%2Fgetting-started%3Fproject%25253Ddirected-smoke-265423%252526pli%25253D1%2526hl%253Den_US&flowName=GlifWebSignIn&flowEntry=ServiceLogin)</b> - For this project I used Google Cloude's virtual machine engine.
2) <b>[Github account](https://github.com/)</b> - I used my github account to store and manage my Graph Theory project
3) <b>sudo apt update </b> - apt is the package manager for debian. Essentially this command tells apt to go the package lists for debian. 
4) <b>sudo apt upgrade</b> - Downloades the newest versions of debian.
5) <b>sudo apt install git</b> - Installer command for git.
6) <b>sudo apt install build-essential</b> - You will need to install gcc. This command installes collections of software for gcc. Build essential is very useful to download for any piece of software because when downloading any code from online sites they tipically require gss.
7) <b>sudo apt install wget</b> - wget is very useful for downloading files.
8) <b>sudo apt install ipython3</b> - On your Google cloud SSH engine you need to download ipython. This downloads python version 3. It is a better environment for creating python programs because it contains various repel effects, formatting and colors.

### Commands to run your code
1) <b>git clone GitLinkHere</b> - This clones the specified GitHub repository into the VM. 
2) <b>ls -al</b> - Shows all files in a directory
3) <b>vi file.py</b> - This command allows you to create a new python file called file.py.
4) <b>vi file.py</b> - By running this command it allows you to view and edit python code in file.py.
5) <b>python file.py</b> - This command runs your python file. It executed the results of your code in file.py.
6) <b>rm file.py</b> - If you wish to delete a file completely you use the rm command along with the file you wish to delete.

## Test
For this project I added numerus classes and functions to test does my code actually work. 

*Classes I used to test my code*
1) <b>prompt.py</b> - This class imports the main class thompson.py as a basis for this testing. I created this class to allow for user input. When python prompt.py is ran the user is met with a series of questions. First they are asked to input a regular expression and then they are asked to enter a string to match the regex with. If they both match a succesful message appears and if not the user is notified that the inputted regular expression des not match the specified string. Users have the oppertunity to ender as much tests as needed. By entering "q" the prompt ends.
2) <b>finaltesting.py</b> - This class imports the main class thompson.py as a basis for this testing. It contains all hardcoded data. Finaltesting.py matches the specified regex with the assigned string. If all data in the class is correct the user is met with a blank answer when finaltesting.py is run. If data is incorrect an error message will appear. I used the "assert" and "assert not" keywords for the implementation of these tests.
3) <b>project.py</b> - At the end of the project.py class I added various tested to see does the infix match the assigned postfix format. The outpus of this class determines do the two formats match. 
4) <b>testing.py</b> - This class imports the main class thompson.py as a basis for this testing. This class uses thompson.match to determine does the regex match the specified string. When ran the console outputs "True" or "False".

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
