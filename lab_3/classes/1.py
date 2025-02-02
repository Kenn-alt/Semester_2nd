class String:
    def __init__(self):
        self.input_string = ''

    def get_input(self):
        self.input_string = input("Enter the number: ")

    def print_input(self):
        print(self.input_string)

my_string = String()

my_string.get_input()
my_string.print_input()