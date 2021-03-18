def names():
    name = str(input("Enter your name: "));

    if set(['a', 'e', 'i', 'o', 'u']).intersection(name.lower()):
        print("Your name contains a vowel.");
    else:
        print("Your name does not contain a vowel.");

    # Iterate over name
    for letter in name:
        print(letter);

# Call the function.
names();