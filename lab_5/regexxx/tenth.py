# Write a Python program to convert a given camel case string to snake case.

# hereIsSomeData -> here_is_some_data

import re

my_text = 'hereIsSomeData'

def change(match):
    return match.group(1) + '_' + match.group(2).lower() # we get the match.group(1) ---> lowercase letters
                                                         # + '_' + match.group(2).lower() ---> turning uppercase letters to lowercase and
                                                         # adding everything together

x = re.sub('([a-z])([A-Z])', change, my_text) # first match: 'eI' ----> \1 -> 'e', \2 -> 'I'
                                              # second match: 'sS' ----> \1 -> 's', \2 -> 'S'
                                              # third match: 'eD' ----> \1 -> 'e', \2 -> 'D'   

print(x)