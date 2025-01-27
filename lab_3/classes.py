# Classes
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
print()

# __init__() function
# Use the __init__ function to assign values to object properties, or other 
# operations that are necessary to do when the object is being created

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 36)

print(person.name)
print(person.age)
print()

# __str__() function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

person = Person("John", 36)
print(person)

# Object Methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("hello, my name is " + self.name)

person = Person("John", 36)
person.my_func()

# The self parameter is a reference to the current instance of the class, and is used to access 
# variables that belong to the class

# We can write anything instead of 'self'


# Modify Object Properties
person.age = 40
print(person.age)

del person.age
del person


# The pass Statement
class Person: 
    pass

