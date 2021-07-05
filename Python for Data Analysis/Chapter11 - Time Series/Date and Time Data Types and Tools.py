from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(now)
print(now.year, now.month, now.day)

delta = datetime(year=2011, month=1, day=7) - datetime(2008, 6, 24, 8, 15)
print(delta)
print(delta.days, delta.seconds)

start = datetime(2011, 1, 7)
print(start + timedelta(days=12))
