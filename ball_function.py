# Example on page 79 of the textbook.

def y(v0, t):  # Beginning of the function named as y
    g = 9.81;
    return v0 * t - 0.5 * g * t ** 2;  # End of the function

v0 = 5;
time = 0.6;

print(y(v0, time));

time = 0.9;
print(y(v0, time));
