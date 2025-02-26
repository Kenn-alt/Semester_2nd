# all() any()
# Write a Python program with builtin function that returns True if all elements of the tuple are true

my_tuple = (True, True, True)

if all(my_tuple):
    print(True)
else: 
    print(False)

# That's how the all() function works (it returns True if the iterable is empty)
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True


# That's how the any() function works (it returns False if the iterable is empty)
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False