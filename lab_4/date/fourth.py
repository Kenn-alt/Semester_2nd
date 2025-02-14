import datetime

# print(todayyy.hour)
# print(todayyy.minute)
# print(todayyy.second)
# print(todayyy.date())

def difference():
    first_input = input("Enter the first date as follows DD-MM-YYYY HH:MM:SS: ")
    second_input = input("Enter the second date as follows DD-MM-YYYY HH:MM:SS: ")

    first_date = datetime.datetime.strptime(first_input, "%d-%m-%Y %H:%M:%S")
    second_date = datetime.datetime.strptime(second_input, "%d-%m-%Y %H:%M:%S")

    diff = abs(first_date - second_date)

    return diff.total_seconds()

print(difference())