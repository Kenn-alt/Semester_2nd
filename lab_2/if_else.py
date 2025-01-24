# Conditional statements
a = 200
b = 300
if a > b:
    print('a is greater than b')
elif a == b:
    print('a is equal to b')
else:
    print('b is greater than a')

# Short Hand If ... Else 
# a.k.a 'Ternary Operator' or 'Conditional Expressions'

a = 2
b = 4
print('a is greater or equal to b') if a >= b else print('b is greater than a')

a = 330
b = 300
print('a is greater than b') if a > b else print('a and b are equal') if a == b else print('b is greater than a')

# Nested If

x = 50

if x > 10:
    print("Above 10")
    if x > 20:
        print("Above 20")
    else:
        print("but not above 20")


# The pass Statement
a = 33
b = 200
if b > a:
    pass