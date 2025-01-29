# A function for permutations of a word
from itertools import permutations

my_str = input("Enter the string: ")

permutat = permutations(my_str)
for p in permutat:
    print(''.join(p))
