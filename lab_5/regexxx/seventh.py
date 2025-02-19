# Write a python program to convert snake case string to camel case string.

import re

my_text = 'some_sample_data'

def to_camel_case(match):
    return match.group(1).upper()

x = re.sub('_([a-z])', to_camel_case, my_text) # we write ([a-z]) to get only the inner group, which is our letter after an underscore '_' 
print(x) # if we write it, [a-z], we will still have our underscores