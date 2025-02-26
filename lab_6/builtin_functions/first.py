# Write a Python program with builtin function to multiply all the numbers in a list

import functools

my_list = [1, 2, 3, 4, 5, 6]

# functools.reduce is for processes a sequence into a single cumulative result

result = functools.reduce(lambda x, y: x * y, my_list) 
print(result)