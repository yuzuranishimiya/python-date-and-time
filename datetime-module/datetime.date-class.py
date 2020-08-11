from datetime import date

# date object to represent a date
d = date(2020, 5, 2)
print("datetime.date(2020, 5, 2):", d)

# get current date
today = date.today()
print("current date:", today)

# get date from timestamp
timestamp = 894042000
date_from_timestamp = date.fromtimestamp(timestamp)
print("timestamp 894042000 equal to Date:", date_from_timestamp)


# print today's year, month and day
today = date.today()
print("current day:", today.day)
print("current month:", today.month)
print("current year:", today.year)