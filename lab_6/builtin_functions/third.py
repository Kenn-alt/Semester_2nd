# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

message = "2002"

reversed_object = reversed(message) # reversed() function returns a reversed iterator, which we can iterate through

reversed_message = ''

for i in reversed_object:
    reversed_message += i

# or we can use .join() method
# res = ''.join(reversed_object)
# print('REs:', res)

if message == reversed_message:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# my_list = [1, 2, 3, 4, 5]

# rev = reversed(my_list)

# res = ''.join(map(str, rev))

# print(res)



