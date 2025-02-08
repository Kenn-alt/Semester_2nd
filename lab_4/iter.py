# Iterator is an object that consists of countable number of values
my_str = 'apple'

my_iter = iter(my_str)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print()


# how for loop works
my_list = ['Apple', "Banana", "Cherry", 'Coconut']

# for i in my_list: 
#     print(i)

looper = iter(my_list)
while True:
    try:
        obj = next(looper)
        print(obj)
    except StopIteration: 
        break



#Creating an Iterator Object/Class

class Nums:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        # In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
my_class = Nums() 
my_iter = iter(my_class) # Now, our class becomes an iterator object 

for x in my_iter: # now we can iterate through the 'my_iter' and print each member of it
    print(x)