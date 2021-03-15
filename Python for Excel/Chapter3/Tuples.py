
currencies = ("EUR", "GBP", "AUD");

print(currencies[0]);

# Concatenating tuples will return a new tuple.
Concatenate = currencies + ("SGD",);

Concatenate2 = currencies + ("SGD",);

print(Concatenate);
print(Concatenate2);
print(currencies);

# Tuples may be constructed in a number of ways:
# Using a pair of parentheses to denote the empty tuple: ()
# Using a trailing comma for a singleton tuple: a, or (a,)
# Separating items with commas: a, b, c or (a, b, c)
# Using the tuple() built-in: tuple() or tuple(iterable)

# Reference: https://docs.python.org/release/3.9.2/library/stdtypes.html?highlight=tuple#sequence-types-list-tuple-range