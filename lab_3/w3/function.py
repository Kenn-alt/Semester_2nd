# *args (Arbitrary Arguments)
# this way the function will receive a tuple of arguments
def my_func(*kids):
    print('The youngest child is ' + kids[2])

my_func('Kevin', 'Thomas', 'John')

print()

# We can also send arguments with the key = value syntax
def my_func(child1, child2, child3):
    print("The kid is " + child3)

my_func(child1 = "Kevin", child2 = "Thomas", child3 = "John")

print()

# kwargs (Keyword Arguments)
# this way the function gets a dictionary of arguments
def my_func(**kid):
    print("His surname name is " + kid['lname'])

print()


my_func(fname = 'Kevin', lname = 'Thomas')

print()

# Default parameters
def my_func(country = "Norway"):
    print("He is from " + country)

my_func("Sweden")
my_func('India')
my_func()
my_func("Brazil")

print()

# Passing a List as an argument
def my_func(food):
    for x in food:
        print(x)

fruits = ['apple', 'banana', 'cherry']
my_func(fruits)

print()

# Return Values
def my_func(x):
    return 5 * x

print(my_func(3))
print(my_func(100))
print(my_func(11))

print()

# Pass statement
def my_func():
    pass

# Positional-Only arguments
# add ', /' after the arguments
def my_func(x, /):
    print(x)

my_func(3)
# my_func(x = 3) this will raise an error
# (because it's a keyword argument)
print()

# Keyword-Only Arguments
# add '*,' before the arguments
def my_func(*, x):
    print(x)

my_func(x = 3)
#my_func(3) this will raise an error 
# (because it's a positional argument)

print()

def my_func(a, b, /, *, c, d):
    print(a + b + c + d)

my_func(5, 6, c = 7, d = 8)

print()

# Recursion

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Result: ")
tri_recursion(6)

