# [letter, for letter in 'shark']
shark_letters = [letter for letter in 'shark']

print(shark_letters)

# shark_letters2 = [letter for item in 'shark']

# When creating a list with a for loop, the variable assigned to the list must be initialized
# with an empty list.
shark_letters = []

for letter in 'shark':
    shark_letters.append(letter)

print(shark_letters)
