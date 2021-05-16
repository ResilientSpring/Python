sammy = {'username': 'sammy-shark',
         'online': True,
         'followers': 987}

print(sammy)

print(sammy.items())

for key, value in sammy.items():
    print(key, 'is the key for the value', value)


print('-----------Separation line---------------')

for key, value in sammy.items():
    print(key, ' is the key for the value ', value)
