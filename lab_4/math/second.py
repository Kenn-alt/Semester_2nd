# Trapezoid
import math

h = int(input("Enter the height of the trapezoid: "))
base1 = int(input("Enter the first base: "))
base2 = int(input("Enter the second base: "))
area = h * (max(base1, base2) + min(base1, base2)) / 2
print("The area:", area)