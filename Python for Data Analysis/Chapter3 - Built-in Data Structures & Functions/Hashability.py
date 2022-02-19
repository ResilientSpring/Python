print(hash('string'))

print(hash((1, 2, (2, 3))))

try:
    print(hash([1, 2]))  # Fails because list is mutable.

except TypeError:
    print("TypeError: unhashable type: 'list'")

try:
    print(hash((1, 2, [2, 3])))  # fails because the third element of the tuple is mutable.

except TypeError:
    print("TypeError: unhashable type: 'list'")
