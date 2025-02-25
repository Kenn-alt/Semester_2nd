# Write a Python program to copy the contents of a file to another file

with open('/Users/kenn_/my_file/Semester_2nd/lab_6/lecture/text.txt', 'r') as my_file_1:
    with open('sample_2.txt', 'w') as my_file_2:
        content = my_file_1.read()
        my_file_2.write(content)
        

# or

# with open('/Users/kenn_/my_file/Semester_2nd/lab_6/lecture/text.txt', 'r') as my_file_1:
#     with open('sample_2.txt', 'a') as my_file_2:
#         for line in my_file_1:
#             my_file_2.write(line)
        