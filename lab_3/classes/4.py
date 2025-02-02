import math
class Point:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_coord(self):
        self.x1 = int(input("Enter the x1 coordinate: "))
        self.y1 = int(input("Enter the y1 coordinate: "))
        self.x2 = int(input("Enter the x2 coordinate: "))
        self.y2 = int(input("Enter the y2 coordinate: "))
    
    def show(self):
        print("x is:", self.x1)
        print("y is:", self.y1)

    def move(self):
        temp = self.x1
        self.x1 = self.y1
        self.y1 = temp
        print("Changed x1:", self.x1)
        print("Changed y1:", self.y1)

    def dist(self):
        print('The distance is', math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)))

my_obj = Point()
my_obj.get_coord()
my_obj.show()
my_obj.move()
my_obj.dist()