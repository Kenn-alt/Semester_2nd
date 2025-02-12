# Sets - unordered and immutable(you can ADD/REMOVE elements). NO duplicates

# 1
# Set - a collection which is unordered, unchangeable(but you can add/remove items)
# and unindexed, do not allow duplicates(duplicates are ignored)
# Set - {}

# Note: the set list is unordered, meaning: the items will appear in a random order.

thisset = {'apple', 'banana', 'cherry'}
print(thisset)

thisset = {'apple', 'banana', 'cherry', 'apple'}
print(thisset)

# the values True and 1 are considered as the same in sets and are treated as duplicates 
# the same with False and 0
thisset = {'apple', 'banana', 'cherry', True, 1}
print(thisset)

# set items can be of any data type and a set contain different data types

# using a Set Constructor
thisset = set(('apple', 'banana', 'cherry'))

# 2 
#looping through a set with 'in' keyword

for x in thisset:
    print(x)

# checking if a value exists in a set
print('banana' in thisset)
print('banana' not in thisset)

# 3
# once a set is created, you cannot change its items, but you can add new items
# add() method is for adding new elements
thisset.add('hello')
print(thisset)

# update() adding items from other collection(list, tuple, set) to a set using update()
new_set = {'kiwi', 'lettuce', 'bread'}
new_set1 = ['world', 'fruit']
thisset.update(new_set)
thisset.update(new_set1)
print(thisset)

# 4
# Removing elements from a set can be done with 1. remove(), 2. discard()
#thisset.remove('strawberry') # remove() will raise an error if elements doesn't exist in a set
#print(thisset)

thisset.discard('banana') # discard() won't raise an error, if element doesn't exist
print(thisset)

# you can pop(), but you won't be sure what you've removed
x = thisset.pop()
print(x)
print(thisset)

# clear() empties the set
thisset.clear()
print(thisset) # Result: set()

# 'del' keyword deletes the set completely
del thisset
#print(thisset) # It will raise an error

# 5 
# using 'for' loop to loop through the set items
thisset = {'apple', 'banana', 'cherry'}
for x in thisset:
    print(x)

# 6 
# Joining sets

# union() - returns a new set with all items from both sets (allows to join sets 
# with other data types, like lists, tuples), (excludes duplicates)
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# we can use '|' instead of the union(), which is the same
set4 = set1 | set2
print(set4)

# joining multiple sets can be done with all methods
set3 = {'apple', 'banana', 'cherry'}
my_set = set1.union(set3, set2)
print(my_set)

# using '|' (it allows to join sets with only sets)
set4 = set1 | set2 | set3
print(set4)

# update() - inserts all items from one set into another (excludes duplicates)
# it changes the original set, and doesn't return a new set
set1.update(set2)
print(set1)

# intersection() - returns elements in both (you can use '&', which will be the same)
set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
set3 = set1.intersection(set2)
print(set3)

# intersection() - allows to join sets with other data types
# '&' allows to join sets with sets only

# intersection_update() - the same, but doesn't return anything, it changes the original set

set1.intersection_update(set2)
print(set1)

# True and 1, False and 1 are the same. The False, True are returned if they're in the
# intesection

# difference() or '-'. '-' for only joining sets with sets
# difference() for joining sets with other data types
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1.difference(set2)
print(set3)

# difference_update() changes the original sets

set2.difference_update(set1)
print(set2)

# shortcut for '-'
set1 -= set2
print(set1)

# symmetric_difference() - elements that are not in both (for joining sets with other data types)
# '^' can also be used (for joining sets with sets only)
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1.symmetric_difference(set2)
print(set3)

# symmetric_difference_update() - changes the original set, doesn't return anything
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set1.symmetric_difference_update(set2)
print(set1)

# 7
# Set Methods

print(set1.isdisjoint(set2))

x = {'a', 'b', 'c'}
y = {'a', 'b', 'c', 'x', 'y', 'z'}
print(x <= y) # we can use 'print(x.issubset(y))'
# '<' - sets cannot be equal, '<=' - sets can be equal

x = {'a', 'b', 'c', 'x', 'y', 'z'}
y = {'a', 'b', 'c'}
print(x >= y) # we can use 'print(x.superset(y))'
# '>' - sets cannot be equal, '>=' - sets can be equal







