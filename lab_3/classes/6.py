def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("Enter the amount of numbers: "))
my_list = [int(input(f"Enter the number {i + 1}: ")) for i in range(n)]

prime_numbers = list(filter(lambda x: is_prime(x), my_list))
print(prime_numbers)