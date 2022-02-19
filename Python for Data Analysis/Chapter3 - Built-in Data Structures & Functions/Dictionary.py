from collections import defaultdict

words = ['apple', 'bat', 'bar', 'atom', 'book']

by_letter = defaultdict(list)

for word in words:
    by_letter[word[0]].append(word)


print(by_letter)
print('\n')
print(words)
