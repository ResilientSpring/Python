# Script 12

items = range(5);

# class range(stop)
# class range(start, stop, step)
#  If the step argument is omitted, it defaults to 1.
#  If the start argument is omitted, it defaults to 0.

# The advantage of the range type over a regular list or tuple is that
# a range object will always take the same (small) amount of memory
# Reference: https://docs.python.org/3.7/library/stdtypes.html#range

print(type(items));

for items in items:
    print(items);