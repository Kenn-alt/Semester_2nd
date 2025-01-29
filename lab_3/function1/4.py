# A function for checking if the number is prime or not
def is_prime(num):
    cnt = 0
    
    if num < 2: 
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
            
    
# A function for filters prime numbers
def filter_prime(numbers):
    my_list = []
    for i in numbers: 
        if is_prime(i):
            my_list.append(i)
    return my_list

n = int(input("Enter the amount of numbers: "))
my_list = [int(input("Enter the number: ")) for _ in range(n)]

print(filter_prime(my_list))
    