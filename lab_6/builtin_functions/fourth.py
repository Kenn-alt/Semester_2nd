# time.sleep()
# Write a Python program that invoke square root function after specific milliseconds.

import time, math

number = int(input("Enter the number: "))
delay = int(input("Enter the delay time in milliseconds: "))

time.sleep((delay / 1000)) # time.sleep() gets seconds as an argument so we divide millisecons by 1000 to get seconds

print(f'Square root of {number} after {delay} milliseconds is {math.sqrt(number)}')