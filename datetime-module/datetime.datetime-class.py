# The datetime module has day_time class named dateclass that can contain information from both date and time objects.
from datetime import datetime

# datetime year, month, day
day = datetime(2020, 5, 2)
print(day)
# more complex
day_time = datetime(2020, 5, 1, 23, 59, 59, 999999)
print(day_time)

# get year, month, day, hour, minutes, second, and timestamp
print("year =", day_time.year)
print("month =", day_time.month)
print("hour =", day_time.hour)
print("minute =", day_time.minute)
print("second =", day_time.second)
print("timestamp =", day_time.timestamp())