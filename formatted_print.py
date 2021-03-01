# Example on page 29 of the textbook

r = 12.89643;         # Real number or float
i = 42;               # integer
s = "some message";   # string  (equivalent: 's = 'some message')

print("real = {:.3f}, integer = {:d}, string = {:s}".format(r, i, s));
print("real = {:9.3e}, integer = {:5d}, string = {:s}".format(r, i, s));

# 9.3e means a scientific notation (e) with 3 decimals, in a field that has a width of 9 characters.

# 5d means an integer in a field that has a width of 5 characters.