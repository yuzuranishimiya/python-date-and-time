# A time object instantiated from the time class represents the local time.
from datetime import time


# Time object to represent time
midnight = time()
print("midnight:", midnight)
midday = time(12,0,0)
print("midday:", midday)
ashar = time(15,15,10)
print("ashar:", ashar, "\n")

# Print hour, minute, second and microsecond from time
magrib = time(18,5,12, 1234)
print("magrib=", magrib)
print("atau")
print(f"magrib= jam:{magrib.hour}, menit:{magrib.minute}, detik:{magrib.second}, microdetik:{magrib.microsecond}")

