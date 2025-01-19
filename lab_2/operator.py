'''

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''

#Arithmetic Operator +, -, *, /, %, **, //

print(2 % 5, '\n')

#Assignment Operators   =, +=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=(walrus operator)


n = 0

while (n := n + 1) < 5: # res: 1 2 3 4 
    print(n)


#Comparison Operators   ==, !=, >, <, >=, <=

print(25 > 20)

#Logical Operators   and, or, not

print(15 > 0 or 'apple' == 'cherry', '\n')

#Identity Operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
# is not

x = 20
y = 25
z = x
print(x is z)

#Membership Operators
x = [1, 2, 3]
print(4 in x)

#Bitwise Operators    &, |, ^, ~, <<, >>

print(15 >> 2)

#Precedence order 
# ()
# **
# +x, -x, ~x
# * / // %
# + -
# << >>
# &
# ^
# |
# == != > >= < <= is is not in not in
# not
# and 
# or 
