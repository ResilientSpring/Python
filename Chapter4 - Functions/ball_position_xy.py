# Example on page 85 of the textbook.

# With default values for all the parameters.
def xy(v0x=2.0, v0y=5.0, t=0.6):
    """Compute horizontal and vertical positions at time t"""
    g = 9.81;
    return v0x * t, v0y * t - 0.5 * g * t ** 2;

x, y = xy();
print("Horizontal position: {:g}, Vertical position: {:g}".format(x, y));

# Some, or all, of the default values may also be overridden:
x, y = xy(v0y=6.0);
print("Horizontal position: {:g}, Vertical position: {:g}".format(x, y));