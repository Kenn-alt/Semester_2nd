# A function for permutations of a word
# from itertools import permutations

# my_str = input("Enter the string: ")

# permutat = permutations(my_str)
# for p in permutat:
#     print(''.join(p))

def permutation(my_str, left = ''):
    if len(my_str) == 0:
        print(left)  
    else:
        for i in range(len(my_str)):
            remainder = my_str[:i] + my_str[i+1:]
            permutation(remainder, left + my_str[i])

a = input("Enter the string: ")
print('The results are:')
permutation(a)