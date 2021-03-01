# Example on page 63 and 64 of the textbook

n = 5;
h = [1.60, 1.85, 1.75, 1.80, 0.50];  # https://www.w3schools.com/python/python_arrays.asp

sum = 0;

for i in range(0, 5, 1):
    sum = sum + h[i];

average = sum / n;

print("Average height: {:f} meters".format(average));