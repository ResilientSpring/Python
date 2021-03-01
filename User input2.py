# Example on page 33 of the textbook

name = input("Hello! What is your name?");

message = input("Hello {:s}! What is your age? ".format(name));

age = int(message);

print("Ok, so you're half way to {}, wow!".format(age * 2));