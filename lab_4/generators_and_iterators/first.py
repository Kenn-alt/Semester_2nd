n = int(input('Enter the number: '))

def squares(n):
    start = 1
    while (start ** 2) <= n: # a generator of squares of integers up to a given n
        yield start ** 2
        start += 1

for i in squares(n):
    print(i)