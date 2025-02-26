# Tuples - ordered and unchangeable(you can't add elements using functions as in lists). Duplicates OK. FASTER than lists
# tuple - ()

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
print(thistuple) # Result: ('apple', 'banana', 'cherry', 'apple', 'cherry')

# To create a tuple with only one item, you have to add a comma after the item, otherwise 
# Python will not recognize it as a tuple

thistuple = ('apple',)
print(type(thistuple).__name__) # Result: tuple

#NOT a tuple
thistuple = ('apple')
print(type(thistuple).__name__) # Result: str

# A tuple can contain different data types

# Using tuple constructor
thistuple = tuple(('apple', 'banana', 'cherry'))
print(thistuple) # ('apple', 'banana', 'cherry')

# 2
thistuple = ('hello', 'world', 'this', 'is', 'a', 'message')
print(thistuple[2:5]) # ('this', 'is', 'a')

if 'apple' in thistuple:
    print("Yes, 'apple' exists in the tuple")

# 3
# We can convert a tuple into a list, change it and convert the list back into a tuple
x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'mango'
y.append("orange")
x = tuple(y)
print(x) # ('apple', 'mango', 'cherry', 'orange')

# It is allowed to add tuples to tuples
thistuple = ('apple', 'banana', 'cherry')
y = ('orange',)
thistuple += y
print(thistuple) # ('apple', 'banana', 'cherry', 'orange')

#Removing elements from tuples by converting to a list
y = list(thistuple)
y.remove('orange')
thistuple = tuple(y)
print(thistuple) # ('apple', 'banana', 'cherry')

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
print(first, second, third) # potato mushrooms ['lettuce', 'dairy', 'mango', 'strawberry', 'raspberry']

(*first, second, third) = products
print(first, second, third) # ['potato', 'mushrooms', 'lettuce', 'dairy', 'mango'] strawberry raspberry

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
print(tuple3) # ('apple', 'banana', 'cherry', 'potato', 'mushrooms', 'lettuce', 'dairy', 'mango', 'strawberry', 'raspberry')

# Multiplying the content by using the '*'
print(thistuple * 3) # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# 7
# Tuple Methods
print(products.count('lettuce')) # 1


print(products.index('strawberry')) # 5
