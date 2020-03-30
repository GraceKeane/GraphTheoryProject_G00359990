# Grace Keane - G00359990
# Graph Theory project 

"""Class for testing thompson's construction by importing
the main script thompson.py. This class determines does
the regular expression match the given string
"""

# Import the main script thompson.py
import thompson

# Random tests & testing Or (|)
assert thompson.match("a*", ""), "True -  should match"
assert thompson.match("a.b|b*", "bbbbbb"), "True - should match"
assert not thompson.match("a.b|b*", "bbx"), "False - should not match"
assert thompson.match("A", "A"), "True - should match"
assert thompson.match("a.c|c*", "cccccc"), "True - should match"

# Concatenate testing (.)
assert thompson.match("a.b", "ab"), "True - should match"
assert thompson.match("a.c", "abc"), "True - should match"
assert thompson.match("a.b", "ab"), "True - should match"
assert not thompson.match("ab", "abc"), "False - should not match"

# Kleene star testing (*)
assert thompson.match("b**", "b"), "True - should match"
assert thompson.match("b*", ""), "True - should match"
assert thompson.match("c**", "c"), "True - should match"

# Plus testing (+)
assert not thompson.match("ab+c", "ac"), "False - should not match"
assert not thompson.match("a+", ""), "False - should not match"
assert thompson.match("b+", "b"), "True -  should match"
assert not thompson.match("ab+", "c"), "False - should not match"
            
# Question testing (?)
assert thompson.match("a?", ""), "True - should match"
assert thompson.match("b?", "b"), "True - should match"
assert not thompson.match("a?", "abcd"), "False - should not match"
assert not thompson.match("abc?", "abv"), "False - should not match"

