# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

with open('/Users/kenn_/my_file/Semester_2nd/lab_5/regexxx/test.txt', 'r') as my_file:
    my_text = my_file.read()

print(re.search('ab{2,3}', my_text))