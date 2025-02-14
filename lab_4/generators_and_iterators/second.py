# printing even numbers between 0 and n 
n = int(input("Enter the number: "))

def even_nums(n):
    start = 0
    while start <= n: # if we put our condition for checking even numbers next to 'start <= n', we'll our function will stop when it would reach 1 won't continue
        if start % 2 == 0:
            yield start
        start += 1

for i in even_nums(n):
    print(i)
