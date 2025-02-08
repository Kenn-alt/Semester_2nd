# A variable created inside a function will exist only inside that function 

def print_num():
    x = 4
    print(x)

print_num()

# the variable is not available outside the function, but it's available for any function inside the function 
def my_func():
    x = 300
    def inner_func():
        print(x)
    inner_func()

my_func()


# a global variable is available on a global and local scopes
y = 200

def my_func1():
    print(200)

my_func1()

# if you write the variable name inside and outside of the function, python will treat them separately

t = 10

def my_func2():
    t = 20
    print(t)

my_func2()

print(t)



# global keyword # 1 
def my_func3():
    global z
    z = 5

my_func3()

print(z)
print()

# changing the global variable inside the function # 2
u = 400

def my_func4():
    global u
    u = 500

my_func4()

print(u)


# 'nonlocal' keyword is used inside nested functions
def my_func5():
    q = 24
    def my_func6():
        nonlocal q
        q = 36
    my_func6()
    print(q)


my_func5()