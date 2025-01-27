# Lambda functions can take any number of arguments
# but can only have one expression

x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5, 6))

z = lambda a, b, c : a + b + c
print(z(5, 6, 2))
print()

# A function that has a lambda function inside, 
# which always doubles the number you send in

def my_func(n):
    return lambda a : a * n

doubler = my_func(2)
tripler = my_func(3)
print(doubler(5))
print(tripler(3))