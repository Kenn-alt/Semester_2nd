class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length = 0):
        self.length = length

    def get_length(self):
        self.length = int(input("Enter the length: "))
    
    def print_area(self):
        print(self.length ** 2)

find_square = Square()

find_square.get_length()
find_square.print_area()