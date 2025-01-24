# 1
# Dictionaries
# items are ordered, changeable, and do not allow duplicates

thisdict = {'brand': "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

# Dictionaries - are changeable, we can change, add, remove items

thisdict = {'brand': "Ford", 'model': "Mustang", 'year': 1964, 'year': 2020, 'colors': ['red', 'green', 'blue']}
print(thisdict)

thisdict = dict(name = 'John', age = 36, country = "Norway")
print(thisdict)

# 2 
#Access items

print(thisdict['age'])
print(thisdict.get('country')) # those two lines are the same

# getting all the keys
print(thisdict.keys()) 

thisdict['color'] = 'white'
print(thisdict.keys())

# getting all the values
print(thisdict.values())

thisdict['age'] = 40
print(thisdict.values())

thisdict['color'] = 'green'
print(thisdict.values())

if 'name' in thisdict:
    print('Yes, the name exists')

# 3
# Change items

thisdict['age'] = 20
print(thisdict)

# Update Dictionary
# if the key doesn't exist, it creates one

thisdict.update({'country': 'Sweden'})
print(thisdict)

# 4
# Add items

thisdict['year'] = 2024
print(thisdict)

thisdict.update({'brand': 'Ford', 'city': "Oslo"})
print(thisdict)

# 5
# Remove items

thisdict.pop('brand') # pop() method
print(thisdict)

thisdict.popitem() # popitem() method
print(thisdict)

del thisdict['year']
print(thisdict)      # 'del thisdict' can delete dictionary completely

# thisdict.clear()  # this method clears the dictionary, but doesn't delete it
# print(thisdict)

# 6
# Loop Dictionaries

# Printing the keys
# for x in thisdict:
#     print(x)

# Printing the values
# for x in thisdict:
#     print(thisdict[x])

# Iterating through the values using the values() method
# for x in thisdict.values(): 
#     print(x)

# Iterating through the keys using the keys() method
# for x in thisdict.keys():
#     print(x)

# Iterating through both keys and values using the items() method
for x, y in thisdict.items():
    print(x, y)

# 7 Copying a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will
# only be a reference to dict1,# and changes made in dict1 will automatically also 
# be made in dict2

# Using copy() method
my_dict = thisdict.copy()
print(my_dict)

# Using dict() method
my_dict = dict(thisdict)
print(my_dict)

# Nested Dictionaries

# Creating a dictionary that contain three dictionaries
my_Family = {
    'child1': {
        'name': "Tilek",
        'year': 1992
    },
    'child2': {
        'name': 'Ayat',
        'year': 1995
    },
    'child3': {
        'name': 'Kenzhe',
        'year': 2006
    }
}

# Creating three different dictionaries and creating one dictionary that will contain them
child1 = {
    'name': "Tilek",
    'year': 1992
}

child2 = {
    'name': 'Ayat',
    'year': 1995
}
child3 = {
    'name': 'Kenzhe',
    'year': 2006
}

my_Family_dict = {
    'child1': child1,
    'child2': child2,
    'child3': child3
}

# Accessing items in Nested Dictionaries
print(my_Family['child1']['name'])

# Looping Through Nested Dictionaries
for x, obj in my_Family.items(): # obj - inner dictionary
    print(x)                    # the name of the inner dictionary

    for y in obj:               # looping the each of the inner dictionaries
        print(y + ':', obj[y])  # key and value of a dictionary

# Dictionary Methods

# The fromkeys() method returns a dictionary with the specified keys and the specified value.
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x) # {'key1': None, 'key2': None, 'key3': None}
print(thisdict)

#setdefault()
# it returns the value of the item, and if it doesn't exist, it inserts the key, 
# with the specified value

x = thisdict.setdefault('brand', 'Ford')
print(thisdict)
print(x)

