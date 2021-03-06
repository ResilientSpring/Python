# Exercise on page 69 of the textbook.

T = float(input("What is the water temperature? ")); # input() returns a string.

if  T > 24:
    print("Great, jump in!");
elif 20 <= T <= 24:
     print("Not bad. Put your toe in first!");
else:
    print("Do not swim. Too cold!");