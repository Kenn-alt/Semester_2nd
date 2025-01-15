import random

x = -1
y = 3.9
z = 2 - 2j

t = -87.7e100

print(type(x), type(y), type(z)) # types: int, float, complex
print(type(t)) # type: float

print(float(x)) # out: -1.0
print(int(y)) # out: 3
print(complex(4)) # out: (4 + 0j)

print(random.randrange(1, 10)) # any number in the range [1, 9]