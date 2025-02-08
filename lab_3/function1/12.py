# A function for creating histograms
def histogram(my_list):
    for i in my_list:
        print('*' * i)


my_list = []
n = int(input("Enter the amount of numbers: "))
for i in range(n):
    num = int(input("Enter the number: "))
    my_list.append(num)

histogram(my_list)


