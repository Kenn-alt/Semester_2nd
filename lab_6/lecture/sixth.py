import os 

path = os.getcwd()

# printing our path '/Users/kenn_/my_file/Semester_2nd/lab_6/lecture/' with the file name that is located in this path

print(path+'/'+'text.txt')

files_and_folders = os.scandir(path) # it returns a scandir iterator

print(files_and_folders)
print(type(files_and_folders))

for element in files_and_folders:
    print(element) # returns the following: 
# <DirEntry 'new_folder'>
# <DirEntry 'fourth.py'>
# <DirEntry 'second.py'>
# <DirEntry 'sixth.py'>
# <DirEntry 'first.py'>
# <DirEntry 'fifth.py'>
# <DirEntry 'text.txt'>
# <DirEntry 'third.py'>

print('----------------------')

files_and_folders = os.scandir(path)


for element in files_and_folders:
    print(element)
    print(element.name)
    print(element.path)
    print(element.path[:-len(element.name)])
    print('-------')
    