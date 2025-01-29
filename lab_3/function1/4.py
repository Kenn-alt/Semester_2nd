# A function for checking if the number is prime or not
def is_prime(num):
    cnt = 0
    for i in range(2, num):
        if num % i == 0:
            cnt += 1
    if cnt > 1:
        return False
    else: 
        return True
    
# A function for filters prime numbers
def filter_prime(numbers):
    my_list = []
    for i in numbers: 
        if is_prime(i):
            my_list.append(i)
    return my_list

n = int(input("Enter the amount of numbers: "))
my_list = [int(input("Enter the number: ")) for i in range(n)]

print(filter_prime(my_list))
    