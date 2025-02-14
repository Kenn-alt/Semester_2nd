# numbers from n to 0

n = int(input("Enter the number greater than 0: "))

def from_n_to_0(n):
    start = n
    while start >= 0: # we get the numbers from n to 0, including 0
        yield start
        start -= 1

for i in from_n_to_0(n):
    print(i)