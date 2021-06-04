sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)

print('Sammy is a ' + sea_creatures[0])

# Stride
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(numbers[1:11:2])

print(numbers[::3])

# Concatenate two or more lists together:
oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']

print(sea_creatures + oceans)

sea_creatures = sea_creatures + ['yeti crab']
print(sea_creatures)

# The * operator can be used to multiply lists.
print(sea_creatures * 2)
print(oceans * 3)
