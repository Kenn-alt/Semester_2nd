# A function for finding the volume
import math
def volume(radius):
    return (4/3) * math.pi * pow(radius, 3)

radius = int(input('Enter the radius: '))
print(volume(radius))
