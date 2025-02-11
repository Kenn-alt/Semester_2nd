class MyClass:
    a = 5

    def __init__(self, b):
        self.b = b

    def print_a():
        print(MyClass.a)

    def print_b(self): # a function of the object is called a 'method' 
        print(self.b)

myclass = MyClass(10)
print(myclass.b) 
print(MyClass.a)
print(myclass.a) # it will work, because all the attributes of classes are available to the objects of those classes

print("------------------------------")


myclass1 = MyClass(15)
myclass2 = MyClass(25)
myclass3 = MyClass(35)


print(myclass1.a, myclass1.b)
print(myclass2.a, myclass2.b)
print(myclass3.a, myclass3.b)

print("------------------------------")

myclass2.a = 789 # 'a' becomes an attribute of the object

print(myclass1.a, myclass1.b)
print(myclass2.a, myclass2.b)
print(myclass3.a, myclass3.b)

print("------------------------------")


MyClass.a = 456

print(myclass1.a, myclass1.b)
print(myclass2.a, myclass2.b) # 789 stays the same for 'a', because it has become an attribute of the object
print(myclass3.a, myclass3.b)

print("------------------------------")

# myclass.print_a() # this will raise an error because 'self' gets passed as the first argument to the function of the class(print_a()) 
MyClass.print_a() # calling a function of the class
myclass.print_b() # callling a function of the object

print("------------------------------")



class Cat: 
    kind = 'feline'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def make_sound(self):
        print('Meow')
    
class HomeCat(Cat):
    def __init__(self, a, b, name, age):
        super().__init__(a, b)
        self.name = name
        self.age = age

garfield = HomeCat('hey', 'hello', 'garfield', 5)

garfield.make_sound()