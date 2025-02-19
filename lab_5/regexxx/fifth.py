import re

with open('/Users/kenn_/my_file/Semester_2nd/lab_5/regexxx/test.txt', 'r') as my_file:
    my_text = my_file.read()

print(re.search('a.*b', my_text))