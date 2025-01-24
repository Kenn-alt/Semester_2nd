# For Loops

# using Break statement
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x == 'banana':
        break

# using Continue Statement
print()
for x in fruits:
    if x == 'banana':
        continue
    print(x)

print()

# using 'else' block 
# printing a message when the loop has ended
for x in range(6):
    print(x)
else:
    print("The end of the range")

print()

# The 'else' will not be executed if loop is stopped by 'break'
for x in range(5):
    if x == 3:
        break
    print(x)
else:
    print("The end of the loop") 

# Nested loop
adj = ['red', 'green', 'blue']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in fruits:
        print(x, y)

# The 'pass' Statement
# 'for loops' cannot be empty, so it you want to leave 'for loop' with no content, 
# put in the 'pass' statement to avoid getting an error

for x in [0, 1, 2]:
    pass