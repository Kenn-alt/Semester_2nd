# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

message = 'HEllo, World, how are you?'

cnt_upper = 0
cnt_lower = 0

for letter in message: 
    if ord(letter) >= 65 and ord(letter) <= 90:
        cnt_upper += 1
    elif ord(letter) >= 97 and ord(letter) <= 122: 
        cnt_lower += 1

print("Uppercase letters:", cnt_upper)
print("Lowercase letters:", cnt_lower)