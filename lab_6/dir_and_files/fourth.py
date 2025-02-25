# Write a Python program to count the number of lines in a text file.

with open('/Users/kenn_/my_file/Semester_2nd/lab_6/lecture/text.txt', 'r') as my_file:
    cnt = 0
    for line in my_file:
        cnt += 1

print(cnt) # Result: 33
