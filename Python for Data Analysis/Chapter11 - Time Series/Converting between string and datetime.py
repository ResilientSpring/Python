from datetime import datetime

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
