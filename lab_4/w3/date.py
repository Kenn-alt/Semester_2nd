import datetime

x = datetime.datetime.now() # year, month, day, hour, minute, second, microsecond
print(x)

# return the year and the name of the weekday
print(x.year)
print(x.strftime('%A'))

print("-----------------")

y = datetime.datetime(2025, 2, 12)
print(y.strftime('%p'))

# %a: Abbreviated weekday name (e.g., "Mon", "Tue", "Wed").
# %w: Weekday as a number 0-6, where 0 is Sunday.
# %d: Day of the month as a number 01-31.
# %B: Full month name (e.g., "January", "February").
# %b: Abbreviated month name (e.g., "Jan", "Feb").
# %m: Month as a number 01-12.
# %Y: Year with century (e.g., 2023).
# %y: Year without century (e.g., 23).
# %H: Hour (24-hour clock) 00-23.
# %I: Hour (12-hour clock) 01-12.
# %M: Minute 00-59.
# %S: Second 00-59.
# %p: AM/PM.

