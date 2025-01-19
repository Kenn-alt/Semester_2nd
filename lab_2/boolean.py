# boolean operator using print()
print(10 + 5)

# using a condition
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# Evaluating values and variables

'''Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones'''

print("#True")
print(bool('abc'))
print(bool(123))
print(bool(['apple', 'banana', 'cherry']))


'''There are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.'''


print("#False")
print(bool(''))
print(bool(0))
print(bool([]))


# A class with __len__ function that returns 0 or False:
class myClass():
    def __len__(self):
        return 0

myobj = myClass()
print(bool(myobj))

#Function returning boolean 

def my_func():
    return True

print(my_func())

#isinstance() can be used to determine if an object is of a certain data type:


print("#isinstance")
x = 200
print(isinstance(x, int))