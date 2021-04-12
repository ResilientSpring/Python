a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x))

# The zip() function returns a zip object, which is an iterator of tuples where the first item
# in each passed iterator is paired together, and then the second item in each passed iterator
# are paired together etc.
#
# If the passed iterators have different lengths, the iterator with the least items decides
# the length of the new iterator.
#
# Source: https://www.w3schools.com/python/ref_func_zip.asp