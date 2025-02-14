from datetime import datetime

print(datetime.now().replace(microsecond = 0)) # replace() is used to modify specific attributes(in our case 'microsecond')
# result: 2025-02-14 19:05:13