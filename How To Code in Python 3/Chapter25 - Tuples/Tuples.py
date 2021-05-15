# A tuple in Python looks like this:
coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')

# Empty tuple
coral_empty = ()

# Tuple with even just one value better uses a comma, as a tuple is meant for grouping data.
coral_one = ('blue coral',)

print(coral, coral_empty, coral_one)

coral_one2 = ('blue coral')
print(coral_one2)

print(coral[0])
print(coral[1])
print(coral[3])
print(coral[-1])
print(coral[-4])

# Concatenate string items in a tuple with other strings using the + operator.
print('This reef is made up of ' + coral[1])
