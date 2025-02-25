# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os

path = '/Users/kenn_/my_file/Semester_2nd/lab_6/lecture'

if os.path.exists(path):
    base = os.path.basename(path)
    print(base) # it returns only the filename 
    print(path[:-len(base)]) # getting the result of the directory which leads to our 'base'