# Example on page 29 of the textbook

v1 = 4;
v2 = 5;

print("v1 is {v1}, \nv2 is {v2}");

print("v1 is {}, \nv2 is {}".format(v1, v2));

print("v1 is {:f}, \nv2 is {:.3f}".format(v1, v2));

print("v1 is %g, \nv2 is %.1f.".format(v1, v2));

print("v1 is %d, \nv2 is %.1f" % (v1, v2));  # old string formatting

print(f"v1 is {v1}, \nv2 is {v2}");  # page 31 of the textbook.

print("v1 is {v1}, \nv2 is {v2}".format(v1=v1, v2=v2));

print("v1 is {v1}, \nv2 is {v2}".format(v2=v2, v1=v1));

print("v1 is {a}, \nv2 is {b}".format(a=v1, b=v2));

print("v1 is {a}, \nv2 is {b}".format(b=v2, a=v1));
