import datetime

# print(todayyy.hour)
# print(todayyy.minute)
# print(todayyy.second)
# print(todayyy.date())

def difference():
    first_input = input("Enter the first date as follows DD-MM-YYYY HH:MM:SS: ") # getting the first date
    second_input = input("Enter the second date as follows DD-MM-YYYY HH:MM:SS: ") # getting the first date

    first_date = datetime.datetime.strptime(first_input, "%d-%m-%Y %H:%M:%S") # getting the first timedelta object
    second_date = datetime.datetime.strptime(second_input, "%d-%m-%Y %H:%M:%S") # getting the second timedelta object

    diff = abs(first_date - second_date) # the difference between the two dates

    return diff.total_seconds() # getting the difference in seconds

print(difference())