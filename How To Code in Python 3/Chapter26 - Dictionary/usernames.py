# Define original dictionary
usernames = {'Sammy': 'sammy-shark', 'Jamie': 'mantisshrimp54'}

# Set up while loop to iterate while True:
while True:
    # Request user to enter a name print('Enter a name:')
    print('Enter a name:')

    # Assign to name variable
    name = input()

    # Check whether name is in the dictionary and print feedback
    if name in usernames:
        print(usernames[name] + ' is the username of ' + name)

    # if the name is not in the dictionary.
    else:
        # Provide feedback
        print('I don\'t have ' + name + '\'s username, what is it?')

        # Take in a new username for the associated name
        usernames = input()

        # Assign username value to name key
        usernames[name] = usernames

        # Print feedback that the data was updated
        print('Data updated')

