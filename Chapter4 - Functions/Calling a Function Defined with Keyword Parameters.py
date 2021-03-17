# Example on the page 84 of the textbook.

# Use 0.6 as a default value for t
def xy(v0x, v0y, t=0.6):
    """Compute horizontal and vertical positions at time t"""
    g = 9.81;  # acceleration of gravity
    return v0x * t, v0y * t - 0.5 * g * t ** 2;

v_init_x = 2.0;  # initial velocity in x
v_init_y = 5.0;  # initial velocity in y

x, y = xy(v_init_x, v_init_y);
print("Horizontal position: {:g}, Vertical position: {:g}".format(x, y));