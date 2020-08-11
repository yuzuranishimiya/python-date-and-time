import datetime

print("What's inside datetime?")
print(dir(datetime), "\n"*2)


# get current date and time
datetime_obj = datetime.datetime.now()
print("datetime:", datetime_obj)


# get current date
date_now = datetime.date.today()
print("date today:", date_now)

