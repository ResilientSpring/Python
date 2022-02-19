immutable = tuple(['foo', [1, 2], True])
print(immutable)

# immutable[1] = [1, 2, 3]

# immutable[1] = immutable[1].append(3)

immutable[1].append(3)

print(immutable)
