# Write a Python program to insert spaces between words starting with capital letters.

import re

my_text = 'HereIsSomeData'

x = re.sub('([a-z])([A-Z])', r'\1 \2', my_text) # first match: 'eI' ----> \1 -> 'e', \2 -> 'I'
                                                # second match: 'sS' ----> \1 -> 's', \2 -> 'S'
                                                # third match: 'eD' ----> \1 -> 'e', \2 -> 'D'      
print(x)