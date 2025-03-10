import json 

data = '{"product": "Laptop", "price": 1200, "brand": "Dell"}'

y = json.loads(data)

y['product'] = 'Phone'

y['price'] = 2400

y['brand'] = 'Apple'

print(y)

new_json_data = json.dumps(y)
print(data)

with open('/Users/kenn_/my_file/Semester_2nd/lab_6/sample.json', 'w') as my_file:
    json.dump(y, my_file)
    