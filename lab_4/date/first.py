from datetime import date, timedelta

def sub_5():
    return date.today() - timedelta(5)

print(sub_5())
