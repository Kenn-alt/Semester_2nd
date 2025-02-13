from datetime import date, timedelta 

def sub_5():
    return date.today() - timedelta(5) # date.today() returns "today's" date, timedelta() returns time duration

print(sub_5())
