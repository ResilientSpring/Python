from collections import defaultdict

words = ['apple', 'bat', 'bar', 'atom', 'book']

by_letter = defaultdict(list)

print(by_letter)

for word in words:
    by_letter[word[0]].append(word)


print(by_letter)
print('\n')
print(words)

print(by_letter[0])
print(by_letter[1])
