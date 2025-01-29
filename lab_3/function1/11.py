# A function for palindrome
def palindrome(my_str):
    if my_str == my_str[::-1]:
        return True
    else:
        return False
    
my_str = input('Enter some string: ')
print(palindrome(my_str))