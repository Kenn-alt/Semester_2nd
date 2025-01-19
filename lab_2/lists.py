# List items are ordered, changeable, and allow duplicate values.

some_list = ['apple', 'banana', 'cherry']
print(some_list)

print(len(some_list))

# lists' data type
print(type(some_list))

# The list() Constructor

this_list = list(('apple', 'banana', 'cherry'))
print(this_list)



#ACCESS LIST ITEMS
some_list_1 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(some_list_1[2:5])

#CHANGE LIST ITEMS

#changing range of items

some_list_3 = ['apple', 'banana', 'cherry']
some_list_3[1:2] = ['blackcurrent', 'watermelon']
print(some_list_3)

some_list_2 = ['apple', 'banana', 'cherry']
some_list_2[1:3] = ['watermelon']
print(some_list_2)

#inserting elements
some_list_4 = ['apple', 'banana', 'cherry']
some_list_4.insert(2, "watermelon")
print(some_list_4)

#ADD LIST ITEMS
#append()
some_list_5 = ['apple', 'banana', 'cherry']
some_list_5.append('orange')
print(some_list_5)

#extend()
tropical = ['mango', 'pineapple', 'papaya']
some_list_5.extend(tropical)
print(some_list_5)

# we can add not only lists, but tuples, sets, dictionaries

#REMOVE LIST ITEMS

some_list_5.remove('mango')
print(some_list_5)

some_list_5.pop(0)
print(some_list_5)

del some_list_5[-1]
print(some_list_5)

some_list_4.clear()
print(some_list_4)

#LOOP LISTS


i = 0
while i < len(some_list_2):
    print(some_list_2[i])
    i += 1

[print(i) for i in some_list_2]



#LIST COMPREHENSION

# newlist = [expression for item in iterable if condition == True]

newlist = [x if x != 'banana' else 'orange' for x in some_list_1]
print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if 'a' in x]
print(newlist)

#SORT LISTS

def myFunc(n):
    return abs(n - 50)

thislist = [100, 50, 62, 82, 23]

thislist.sort(key = myFunc)
print(thislist)

# sort() is 'case sensitive' - all capital letters are sorted before lower case letters
# to make it 'case insensitive' - use 'key = str.lower'

thislist.reverse()
print(thislist)

#COPY LISTS
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

my_list = thislist.copy()
print(my_list)

my_list = list(thislist)
print(my_list)

#using slice operator
my_list = thislist[:]
print(my_list)  

#JOIN LISTS

#using '+'
print(my_list + thislist)

#using extend
my_list.extend(thislist)
print(my_list)

#LIST METHODS


#count()
fruits = ['apple', 'banana', 'cherry']
print(fruits.count('apple'))

#index() - The index() method only returns the first occurrence of the value
print(fruits.index('apple'))

#remove() - The remove() method removes the first occurrence of the element with the specified value.
fruits.remove('cherry')
print(fruits)