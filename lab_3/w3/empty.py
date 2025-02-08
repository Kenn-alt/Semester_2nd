class Shape:
    def __init__(self, length = 0, width = 0):
        self.length =  length 
        self.width = width 


class Parallelepiped(Shape):
    def __init__(self, length, width, height = 0):
        super().__init__(length, width)
        self.height = height 

    def get_length(self):
        self.length = int(input("Enter some number for length: "))

    def get_width(self):
        self.width = int(input("Enter some number for width: "))
        
    def get_height(self):
        self.height = int(input("Enter some number for height: "))

    def volume(self):
        vol = self.length * self.width * self.height 
        return vol



obj = Parallelepiped(15, 10, 20)

obj.get_length()
obj.get_width()
obj.get_height()

print(obj.volume())