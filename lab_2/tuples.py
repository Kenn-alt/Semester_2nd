# Tuples - ordered and unchangeable(you can't add elements using functions as in lists). Duplicates OK. FASTER than lists


# 1
# Dynamic typing - you can change the type of the variable after it is created

a = 5
print(type(a).__name__) # int

# Strings in Python - they cannot be changed after they are created

a = True
b = True
print(a + b + b) # 3

# Tuple - a collection which is ordered, unchangeable(immutable) and allow duplicate values

# tuple - ()

thistuple = ("apple", 'banana', 'cherry', "apple", 'cherry')
print(thistuple)

# To create a tuple with only one item, you have to add a comma after the item, otherwise 
# Python will not recognize it as a tuple

thistuple = ('apple',)
print(type(thistuple).__name__)

#NOT a tuple
thistuple = ('apple')
print(type(thistuple).__name__)

# A tuple can contain different data types

# Using tuple constructor
thistuple = tuple(('apple', 'banana', 'cherry'))
print(thistuple)

# 2
thistuple = ('hello', 'world', 'this', 'is', 'a', 'message')
print(thistuple[2:5])

if 'apple' in thistuple:
    print("Yes, 'apple' exists in the tuple")

# 3
# We can convert a tuple into a list, change it and convert the list back into a tuple
x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'mango'
y.append("orange")
x = tuple(y)
print(x)

# It is allowed to add tuples to tuples
thistuple = ('apple', 'banana', 'cherry')
y = ('orange',)
thistuple += y
print(thistuple)

#Removing elements from tuples by converting to a list
y = list(thistuple)
y.remove('orange')
thistuple = tuple(y)
print(thistuple)

del x # deleting completely

# 4
# 'Unpacking' - extracting values back into variables
products = ('potato', 'mushrooms', 'lettuce')
(first, second, third) = products
print(first, second, third)

# IF the number of variables is less than the number of values, use an *(asterisk) to the variable name 
# and the values will be assigned to it as a list

products = ('potato', 'mushrooms', 'lettuce', 'dairy', 'mango', 'strawberry', 'raspberry')
(first, second, *third) = products
print(first, second, third)

(*first, second, third) = products
print(first, second, third)

# 5
for x in products:
    print(x)

print()

i = 0
while(i < len(products)):
    print(products[i])
    i += 1

# 6
# Joining tuples using '+'
tuple3 = thistuple + products
print(tuple3)

# Multiplying the content by using the '*'
print(thistuple * 3)

# 7
# Tuple Methods
print(products.count('lettuce'))


print(products.index('strawberry'))
