# Write a Python program to split a string at uppercase letters.

import re

my_text = 'There Is Some Sample Text'

x = re.split(r'(?=[A-Z])', my_text) # we group words to get the strings that start with 'A-Z' and has zero or more characters after
print(x[1:])                          # if we don't write '?=', we would erase the found characters [A-Z] ---- we keep them using '?=', which 
                                      # is called 'lookahead assertion' ---> it keeps everything inside the () brackets
                                      # Example: if we write --- r",(?= )" --- the match is a comma followed by the space. 
                                      # If we find a match we split our string at this place, but keep everything inside brackets, 
                                      # which is the space
                                      # re.split() -> splits everything before and after the match



# Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion.
# For example, Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.