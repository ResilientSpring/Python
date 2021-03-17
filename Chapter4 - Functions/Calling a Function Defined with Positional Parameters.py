# Page 82 of the textbook

def y(v0, t):
    g = 9.81;   # Acceleration of gravity
    return v0 * t - 0.5 * g * t**2;

# Mixing the Position of Arguments
print(y(5, 0.6));  # Works fine
print(y(0.6, 5));  # Gives no error message, but the wrong result!

initial_velocity = 5;
time = 0.6;
print(y(initial_velocity, time)); # works fine.
print(y(time, initial_velocity)); # No error message, but wrong result!

# Using Keywords in the Call
print(y(v0=5, t=0.6));        # Works fine.
print(y(t=0.6, v0=5));        # Order switched, works fine with keywords!

# Mixing positional and keyword arguments in the call.
v0 = 5;
print(y(v0, t=0.6)); # Works fine!
# print(y(t=0.6, v0)); Gives syntax error! 