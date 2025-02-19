# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

with open('/Users/kenn_/my_file/Semester_2nd/lab_5/regexxx/test.txt', 'r') as my_file:
    my_text = my_file.read()


print(re.findall('[A-Z][a-z]+', my_text))
