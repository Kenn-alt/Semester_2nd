from datetime import timedelta, date

def get_yesterday():
    return date.today() - timedelta(1)

def get_tomorrow():
    return date.today() + timedelta(1)


print("Yesterday:", get_yesterday())
print("Today:", date.today())
print("Tomorrow:", get_tomorrow())