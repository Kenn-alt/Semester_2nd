# Strings in python 
print("Hello", 'hello')

print("It was 'hilarious'")

a = "hello"
print(a)

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

c = """hello
world"""


# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
print(a[1])


# Since strings are arrays, we can loop through the characters in a string, with a 'for' loop.
for x in "apple":
    print(x)


# finding the length of a string 
print(len(c))

# finding the string inside a string
text = "The best things in life are free"
if "The" not in text:
    print("'The' doesn't exists in the text")

# slicing strings
a = " hello, world! "
print(a[3:5])
print(a[:5])
print(a[2:])
print(a[-5:-2])

# modifying strings
print(a.upper())
print("Great".lower())
print(a.strip())
print(a.strip().replace('ello', 'ow are you'))
print(a.split(','))


# Concatenation
a = "Hello"
b = "World"
print(a + " " + b)

# Format strings
age = 18
print(f"I'm {age} years old")


price = 100
print(f'Bread is {price} tenge')

# displaying the price with 2 decimals
print(f"It costs {price:.2f} dollars")

# Performing a math operation in the placeholder
print(f'It costs {20 * 10} dollars')


# Escape characters
print("We are the so-called \"Vikings\" from the north.")

# String Methods
a = "HellLlo, world!"

print(a.capitalize())
print(a.casefold())
print(a.center(20, ','))
print(a.count('l'))
print(a.find('H'))
x = "I'm Jerry, and I'm {years:.2f} years old"
print(x.format(years = 18)) # out: I'm Jerry, and I'm 18 years old"
print(x.find('J'))
print(x.isalnum())
print(x.isalpha())
print("Salem".isascii())
b = '\u0030'
print(b.isdecimal())
print(a.isdigit())
print("my_file".isidentifier())
print(a.islower())
print(a.isnumeric())
print('\nhello'.isprintable())
print('   '.isspace())
print('Hello, World'.istitle())
print('Hello, world'.isupper())
a = ['a', 'b', 'c']
print('.'.join(a))
a = 'banana'
print(a.ljust(20), 'is my favorite fruit')
print('SALEM'.lower())
a = '    banana    '
print(a.lstrip(), 'is my favorite fruit')
txt = "Mi casa, su casa"
print(txt.rfind('casa'))
a = 'banana'
print(a.rjust(10, 'k'), 'is my favorite fruit')
txt = "I could eat bananas all day, bananas are my favorite fruit" #The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
print(txt.rpartition('bananas'))
print(txt.rsplit(','))
txt = "banana,,,,,ssqqqww....."
print(txt.rstrip(",.qsw"))
print(txt.split(','))
txt = "apple#banana#cherry#orange"
print(txt.split('#', 1))
txt = "Thank you for the music\nWelcome to the jungle"
print(txt.splitlines(True))
txt = "Hi, welcome to the country"
print(txt.startswith("Hello"))
txt = ",,,,,rrttgg.....banana....rrr"
print(txt.strip(",.rtg"))
txt = "Hi, my name is Kenzhe"
print(txt.swapcase())
txt = "hello b2b2b2 and 3g3g3g"
print(txt.title())

my_dict = {83: 80}
txt = "Hello, Sam!"
print(txt.translate(my_dict))


txt = "Hello, Sam!"
mytable = txt.maketrans('S', 'P') # x - what to replace, y - corresponding characters to replace with, z - characters to remove
print(txt.translate(mytable))

print(txt.upper())

a = "10"
print(a.zfill(10))
b = "10.0"
print(b.zfill(10))
c = "Welcome, to the country"
print(c.zfill(10))