# A timedelta object represents the difference between two dates or times.
from datetime import timedelta


# Difference between two timedelta object
t1 = timedelta(weeks=1, days=3, hours=2, minutes=10)
t2 = timedelta(weeks=0, days=6, hours=4, minutes=12, seconds=10)
t3 = t1 - t2
print("range time t1 to t2:", t3)

# Printing Negative Timedelta object
t1 = timedelta(weeks=1, days=1, hours=12, minutes=55, microseconds=12234)
t2 = timedelta(weeks=3, days=6, hours=9, minutes=12, seconds=40)
t3 = t1 - t2
print("range time t1 to t2:", t3)


# time duration in second
t = timedelta(days=10, hours=2, seconds=44, microseconds=231412)
print("total second=", t.total_seconds())
