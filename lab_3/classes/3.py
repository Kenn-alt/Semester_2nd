class Shape:
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width

    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        super().__init__(length, width)
        
    def get_length(self):
        self.length = int(input("Enter the length: "))
    
    def get_width(self):
        self.width = int(input("Enter the width: "))

    def print_area(self):
        print("The area is", self.width * self.length)

get_rect_area = Rectangle()
get_rect_area.get_length()
get_rect_area.get_width()
get_rect_area.print_area()


