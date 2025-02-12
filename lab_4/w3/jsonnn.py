import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x) # loads() method is for converting from json to python

print(y['age'])

t = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

z = json.dumps(t)

print(z)

print('------------------')
# Converting from python to json 

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(['apple', 'banana']))
print(json.dumps(('apple', 'banana')))
print(json.dumps('hello'))
print(json.dumps(12))
print(json.dumps(14.12))
print(json.dumps(True))
print(json.dumps(None))

print('------------------')

r = {
    "name" : 'John', 
    'age' : 30, 
    'married' : True,
    'divorced' : False, 
    'children' : ("Ann", "Billy"), 
    'pets' : None, 
    'cars' : [
    {'model' : "BMW 230", 'mpg' : 27.5},
    {"model" : "Ford Edge", 'mpg' : 24.1}
    ]
}

print(json.dumps(r, indent = 4, separators = ('. ', ': '), sort_keys = True)) # sort_keys = True sorts the result by the keys
# separators has two parameters, 1. separates each object 2. separates keys and values