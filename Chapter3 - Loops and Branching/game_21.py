# Example 3.8 on page 75 of the textbook

import random

ransom = 0;
total_sum = 0;
i = 0;

while i == 0:

    condition = input("Draw a random variable? Y/N");

    if condition == 'Y':
        ransom = random.randint(0, 10);
        total_sum += ransom;

        print("You drew {:d}, making the sum become {:d}".format(ransom, total_sum));

    if total_sum > 21:
        print("You are out of the game because the sum reached {:d} and passed 21."
              .format(total_sum));
        break;