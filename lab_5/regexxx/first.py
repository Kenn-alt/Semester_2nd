# * ---- zero or more of characters
# + ---- one or more of characters
# \b ---- matches the boundary between a word and a non-word character.

# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

with open('/Users/kenn_/my_file/Semester_2nd/lab_5/regexxx/test.txt', 'r') as my_file:
    my_text = my_file.read()



x = re.search('ab*', my_text)
print(x)

