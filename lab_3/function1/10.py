# A function that finds unique elements of a set
def unique_set(my_list):
    my_list_unique = []
    for i in my_list:
        if i not in my_list_unique:
            my_list_unique.append(i)
    return my_list_unique

my_list = []

n = int(input("Enter the amount of numbers: "))
for i in range(n):
    num = int(input("Enter the number: "))
    my_list.append(num)
print(unique_set(my_list))