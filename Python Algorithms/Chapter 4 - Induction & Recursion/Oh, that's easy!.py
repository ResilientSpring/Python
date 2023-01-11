from random import randrange

sequence = [randrange(10**10) for i in range(100)]

dd = float("inf")

for x in sequence:
    for y in sequence:

        if x == y:
            continue

        d = abs(x - y)

        if d < dd:
            xx, yy, dd = x, y, d

            print(xx, yy)




