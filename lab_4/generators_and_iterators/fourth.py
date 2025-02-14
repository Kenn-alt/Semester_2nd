# squares between a and b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def squares_a_b(a, b):
    start = 1
    while start ** 2 <= b: # the 'while' loop works until we reach the 'b'
        if start ** 2 >= a: # if our the square of 'start' is greater or equal to a, yield it, 
            yield start ** 2
        start += 1 # otherwise just increment 'start' by 1

for i in squares_a_b(a, b):
    print(i)
