a = [1, 2, 3];
b = a;
c = list(a);

# To check if two references refer to the same object, use the is keyword.
print(a is b);

# is not is also perfectly valid if you want to check that two objects are not the same.
print(a is not c);
