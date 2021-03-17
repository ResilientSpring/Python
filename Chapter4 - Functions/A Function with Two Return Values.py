# Page 84 of the textbook

def xy(v0x, v0y, t):
    """Compute horizontal and vertical positions at time t"""
    g = 9.81;   # Acceleration of gravity
    return v0x * t, v0y * t - 0.5 * g * t ** 2;

v_init_x = 2.0;    # initial velocity in x
v_init_y = 5.0;    # initial velocity in y
time = 0.6;        # chosen point im time

# The order of the results returned from the function must be the same as the order of
# the corresponding variables in the assignment statement.
x, y = xy(v_init_y, v_init_y, time);
print("Horizontal position: {:g}, Vertical position: {:g}".format(x, y));