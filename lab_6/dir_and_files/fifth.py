# Write a Python program to write a list to a file.

my_list = ['1. apple', '2. banana', '3. cherry', '4. mango']

with open('/Users/kenn_/my_file/Semester_2nd/lab_6/dir_and_files/sample.txt', 'w') as my_file:
    for fruit in my_list:
        my_file.write(fruit + '\n')

