import re
# RegEx - Regular Expressions ---- a sequence of characters that forms a search pattern.

# functions - 1.findall() - all matches
            # 2.search() - returns Match object if it's found(if there's more than one, it returns the first occurence)(Otherwise, it returns 'None')
            # 3.split() - list where the string has been split at every match
            # 4.sub() - replaces one or many matches with a string

# Metacharacters
# Examples
# '[a-m]'
# '\d' - all digits
# 'he..o' - 'he' any two characters and 'o'
# '^hello' - starts with 'hello'
# 'planet$' - ends with 'planet' 
# 'he.*o' - zero or more occurences
# 'he.+o' - one or more occurences
# 'he.?o' - zero or one occurence
# 'he{3}.o' - exactly three characters after 'he' and before 'o' 
# 'hello|bye' - one of the two words 

# Special Sequences 
# \A ---- '\AThe' - if it's found at the beginning of a string
# \b ---- r'\bword' - if it's at the beginning -------- the 'r' before a string indicates 'raw string', which means we ignore escape characters
        # r'word\b' - if it's at the end 
# \B ---- r'\Bword' - if it's present, but not at the beginning
        # r'word\B' - if it's present, but not at the end
# \d ---- numbers from 0 to 9
# \D ---- returns all nondigit characters
# \s ---- returns all whitespace characters (when working with 'findall()')
# \S ---- Finds all nonwhitespace characters (when working with 'findall()')
# \w ---- return all 'a' to 'z', 'A' to 'Z', 0-9, '_' characters (when working with 'findall()')
# \W ---- returns all nonword characters(including '!', '?', whitespace) (when working with 'findall()')
# \Z('Spain\Z') ---- True if specified characters are at the end of the string

# [abc] ---- if one of the characters is present
# [a-h] ---- returns the interval of lowercase letters that present
# [^abc] ---- any character, except 'abc'
# [01234] ---- returns a match if one of 0, 1, 2, 3, 4 is present
# [0-7] ---- a match for any digit between 0-7
# [0-7][0-7] ---- a match for two digit numbers 
# [a-zA-Z] ---- match if any characters from a-z or A-Z
# in sets +, *, ., |, (), $, {} has no special meaning, so [+] returns a match if '+' is present in the string


# re.split()
txt = "The rain in Spain"

x = re.split('\s', txt) # splits by whitespaces
# ['The', 'rain', 'in', 'Spain']

print(x)

x = re.split('\s', txt, maxsplit = 1) # splits with 'maxsplit' parameter equal to 1. Result: ['The', 'rain in Spain']

# re.sub()
x = re.sub('\s', '7', txt) # replaces all whitespaces with 7
print(x)
# Result: The7rain7in7Spain

x = re.sub('\s', '7', txt, count = 2) # controlling the number of replacements by specifying the 'count' parameter
print(x) 
# Result: The7rain7in Spain



# Match Objects has 3 properties
# 1. .span() ---- a tuple containing start and end(excluding) of the match
# 2. .string() ---- a string that passed into the function 
# 3. .group() ---- returns the part of the string where there was a match 


x = re.search(r'\bS\w+', txt) # searches for a word that begins with "S" followed by one or more word characters.
print(x.span()) # returning the span of the occurence
print(x.string) # returning the string that was passed into the function 
print(x.group()) # returns the part of the string where there was a match 
# If there's no match, 'None' is returned