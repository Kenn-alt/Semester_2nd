import os

path = '../'

# .. - shorthand for previous directory 
# . - shorthand for current directory 

contents = os.listdir(path)

for i in contents: 
    print(i)