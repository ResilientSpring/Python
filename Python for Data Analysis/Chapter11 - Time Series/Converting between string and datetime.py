from datetime import datetime

import pandas as pd
from dateutil.parser import parse

stamp = datetime(year=2011, month=1, day=3)
print(stamp)
print(30*'=')
print(str(stamp))
print(30*'=')
print(type(stamp))
print(30*'=')
#print(stamp.strftime(fmt='%Y-%m-%d'))
print(stamp.strftime('%Y-%m-%d'))

print(30*'=')

# Convert strings to dates
value = '2011-01-03'
# value2 = datetime.strptime(date_string=value, format='%Y-%m-%d')
# print(value2)
value3 = datetime.strptime(value, '%Y-%m-%d')
print(value3)

datestrs = ['7/6/2011', '8/6/2011']
print(type(datestrs))
surely = [datetime.strptime(x, '%m/%d/%Y') for x in datestrs]
print(surely)
print(type(surely))

tangible = [x for x in datestrs]
print(tangible)
print(type(tangible))

stringent = '2011-01-03'
print(type(stringent))

parse(stringent)
print(stringent)
print(type(stringent))

stringent2 = parse(stringent)
print(stringent2)
print(type(stringent2))

complicit = 'Jan 31, 1997, 10:45 PM'
dipstick = parse(complicit)
print(dipstick)

recumbent = parse('6/12/2011')
print(recumbent)

hindrance = parse('6/12/2011', dayfirst=True)
print(hindrance)

print(parse('6/12/2011', dayfirst=True))

datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
edutainment = pd.to_datetime(datestrs)
print(edutainment)

idx = pd.to_datetime(datestrs + [None])
print(idx)
