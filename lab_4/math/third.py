# Area of a Polygon
import math

n = int(input("Enter the number of sides of the polygon: "))
length = int(input("Enter the length of a side: "))
apothem = length / (2 * math.tan(math.radians(180 / n))) # tan() function takes radians

area = int((n * length * apothem) / 2) # or we can round the result with 'round(area, 2)', so that we would have at most 2 decimal points

print("The area of the polygon:", area)