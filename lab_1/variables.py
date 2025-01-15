#creating a variable and assigning a value to it
x = 5
y = "World"

print(x, y)

x = "Kevin"

print(x)

#type casting 

a = str(4)
b = int(4)
c = float(4)

print(a, b, c) 


# finding the type of a variable
print(type(a))

abc = "How are you?"
Abc = 'How are you?'



print(a)
print(b)


# variables in python are case-sensitive
a = 1
A = 'Green'

print(a, A)


# many values to multiple variables
var1, var2, var3 = "Apple", "Pie", "Cherry"

print(var1, var2, var3)


# one value to multiple variables
x = y = z = "Salem"

print(x, y, z)


# unpacking a collection
products = ["Apple", "Pie", "Cherry"]
x, y, z = products

print(x, y, z)


# outputing variables
x = "Python is awesome"
print(x)


# outputing many variables
x = 'Python'
y = 'is'
z = 'awesome'
print(x, y, z)
print(x + y + z)


# adding values of the variables
x = 5
y = 10
print(x + y)



# This will give an error
# x = 5
# y = "Naruto"
# print(x + y)  

# Global variables
x = "awesome"
def myFunc():
    print("Python is", x) # result: 'Python is awesome's

myFunc()



y = 'Wonderful'
def Function():
    y = "Excellent"
    print("Python is", y)

Function()

print("Python is", y) # result: 'Python is Excellent'


# using 'global' keyword
def Myfunc():
    global z
    z = "Amazing"
    print('Python is', z) # result: 'Python is Amazing'

Myfunc()




t = "Incredible"

def funct():
    global t
    t = 'amazing'

funct()

print("Python is", t) # result: 'Python is amazing' 