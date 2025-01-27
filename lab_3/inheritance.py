# Python Inheritance

# Parent class - the class being inherited from, also called the 'base' class
# Child class - the class that inherits from another class, also called 'derived' class

# Create a Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()



# Create a Child Class
# To create a child class, sent the parent class as a parameter
class Student(Person):
    pass # Use the 'pass' keyword when you do not want to
         # add any other properties or methods to the class

x = Student("Mike", "Olsen")
x.printname()



# Adding __init__() function to the child class
class Student(Person):
    def __init__(self, fname, lname): # when you add the __init__(), the child class will
        pass                          # no longer inherit the parent's __init__()

# To keep the inheritance of the parent's __init__(), 
# add a cal to the parent's __init__()
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()



# super() allows child class inherit all the methods and properties from its parent
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    
x = Student("Kevin", "Anderson")
x.printname()
# By using the 'super()', you do not have to use the name
# of the parent element, it will inherit the methods and properties from its parent



# Adding Properties
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Thomas", 'Mozart')
x.printname()

# Adding a 'year' parameter and passing it when creating objects
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
x.printname()



# Adding Methods
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome,", self.firstname, self.lastname + ', to the class of', self.graduation_year)
    
x = Student("Mike", "Olsen", 2025)
x.welcome()

# If you add a method in the child class with the same name
# as a function in the parent class, the inheritance of the parent class
# will be overridden

