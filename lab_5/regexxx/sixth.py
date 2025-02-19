# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

my_text = "Helllo. how are you, what's up"

def change(match): # 'change()' changes our match with colon
    return ":"

x = re.sub('[.,\s]', change, my_text) # finding characters that are either a dot, comma or a whitespace and whenever it's found -> call the function 'change'
print(x)