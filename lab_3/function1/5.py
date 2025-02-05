# A function for permutations of a word
# from itertools import permutations

# my_str = input("Enter the string: ")

# permutat = permutations(my_str)
# for p in permutat:
#     print(''.join(p))

def permutation(my_str, left = ''): # the permutation is stored in the 'left' variable
    if len(my_str) == 0: # if the string is empty, we just print the permutation
        print(left)  
    else:
        for i in range(len(my_str)): # we go back and forth in our for loop, while deepening in every permutation until we get an empty string
            remainder = my_str[:i] + my_str[i+1:]
            permutation(remainder, left + my_str[i]) # calling our function with arguments (remainder and the characters added to the string 'left')

a = input("Enter the string: ")
print('The results are:')
permutation(a)