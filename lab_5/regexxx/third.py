# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

with open('/Users/kenn_/my_file/Semester_2nd/lab_5/regexxx/test.txt', 'r') as my_file:
    my_text = my_file.read()

print(re.findall('[a-z]+_', my_text))