file_names = ["one.xlsx", "two.xlsx", "three.xlsx"];
numbers = [1, 2, 3];
print(file_names + numbers);

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
cells = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(cells[1]);

print(cells[1][1:]);

users = ["Linda", "Brian"];
users.append("Jennifer"); # Most commonly you add to the end.

print(users);

users.insert(0, "Kim"); # insert "Kim" at index 0
print(users);

# To delete an element, use either pop or del. While pop is a method, del is implemented
# as a statement in Python.
print(users.pop()); # Removes and returns the last element by default.
print(users);

del users[0]; # del removes an element at the given index.
print(users);

print(len(users)); # Length
print("Linda" in users); # Check if users contains "Lindas".

print(sorted(users)); # Returns a new sorted list.
print(users); # The original list is unchanged.

users.sort(); # Sort the original list.
print(users);