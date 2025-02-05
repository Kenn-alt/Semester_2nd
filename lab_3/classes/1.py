class String:
    def __init__(self): # Everything we write in '__init__()' is for creating attributes inside a class
        self.input_string = '' # 'self.variable' is an attribute and we assign values from an object to it

    def get_input(self):
        self.input_string = input("Enter the number: ") # we use variables 'self.variable' inside our classes in 'methods' 

    def print_input(self):
        print(self.input_string)

my_string = String() # we don't need pass anything to the 'self' parameter

my_string.get_input()
my_string.print_input()