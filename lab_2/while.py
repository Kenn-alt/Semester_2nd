# While loop 
# it works until the condition is true

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)     # Result: 1 2 4 5 6 

print()

# Printing a message once the condition is false
i = 0
while i < 6: 
    print(i)
    i += 1
else:
    print("i is no longer less than 6")