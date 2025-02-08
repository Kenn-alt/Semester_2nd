from modules import person1 # 'as mx'    # importing only parts from a module

import platform 

# When using a function from a module, use the syntax: module_name.function_name.

# mx.Hello()

# a = mx.person1
# print(a)

a = person1
print(a)



# Other built-in modules in python
x = platform.system()
print(x)


# dir() is used to return the list with all the functions and variables in a module 
y = dir(platform)
print(y)

# z = dir(mx)
# print(z)

# When importing using the from keyword, do not use the module name when referring to elements in the module. 
# Example: person1["age"], not mymodule.person1["age"]