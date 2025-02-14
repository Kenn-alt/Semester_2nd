# numbers divisible by 3 and 4 between 0 and n 

n = int(input("Enter the number: "))

def div_3_4(n):
    start = 0
    while start <= n:
        if start % 3 == 0 and start % 4 == 0:
            yield start
        start += 1
    
for i in div_3_4(n):
    print(i)