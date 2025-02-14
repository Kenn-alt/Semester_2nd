import json


# we use the function 'load()' to get we're working with file objects(our 'my_file' is 'file object')
# we use the function 'loads()' when working with a string that contains JSON data in it 
with open('/Users/kenn_/my_file/Semester_2nd/lab_4/json/sample-data.json', 'r') as my_file: # opening a json file as file
    data = json.load(my_file) # getting a dictionary from the content of a json file 

print('Interface Status')
print('=' * 78)

DN = "DN"
Description = 'Description'
Speed = 'Speed'
MTU = 'MTU'

print(f"{DN:<50} {Description:<20}  {Speed:<8} {MTU:<5}") # :<20 is for left-alignment of words in a field of 20 characters
print('-' * 50 + " " + '-' * 20 + "  " +  '-' * 6 + "  " +  '-' * 6)


for item in data['imdata']: # data['imdata'] is a list 
    attributes = item['l1PhysIf']['attributes'] # every ith element of data['imdata'] contains a dictionary with only one key 'l1PhysIf', which has a value of dictionary 'attributes' 
    # the dictionary 'attributes' contains many keys 
    dn = attributes.get('dn') 
    description = attributes.get('descr', '') # we'll get an empty string '' as a default if it's missing 
    speed = attributes.get('speed', 'inherit') # we'll get 'inherit' as a default if it's missing 
    mtu = attributes.get('mtu', '') # we'll get an empty string '' as a default if it's missing 
    print(f"{dn:<50} {description:<20} {speed:<9} {mtu:<5}")
