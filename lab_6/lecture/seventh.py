file_name = 'text.txt'

file = open(file_name, 'r')

print(f'File {file_name} is closed:', file.closed) # checking if the file is closed

file.close()

print(f'File {file_name} is closed:', file.closed)

print('---------------')

with open(file_name, 'r') as my_file:
    print(f'File {file_name} is closed:', my_file.closed) # our file is not closed while it's in the block of 'with'

print(f'File {file_name} is closed:', my_file.closed) # it's closed after the leave the block of 'with'

print('------------------')

with open(file_name, 'r') as file: # printing first three lines
    print(file.readline(), end = '')
    print(file.readline(), end = '')
    print(file.readline(), end = '')


print('--------------------')

with open(file_name, 'r') as my_file:
    for line in my_file:
        print(line, end = '')


