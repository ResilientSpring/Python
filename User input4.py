name = input("What is your name?");

message = "Hello {:s}! What is your age? ".format(name);

age = int(input(message));
print("Ok, so you are half way to {}, wow!".format(age * 2));