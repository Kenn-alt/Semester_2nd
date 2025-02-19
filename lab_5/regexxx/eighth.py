# Write a Python program to split a string at uppercase letters.

import re

my_text = 'There Is Some Sample Text'

x = re.split(r'(?=[A-Z].*)', my_text) # we group words to get the strings that start with 'A-Z' and has zero or more characters after
print(x[1:])                          # if we don't write '?=', we would erase the found characters [A-Z] ---- we keep them using '?='