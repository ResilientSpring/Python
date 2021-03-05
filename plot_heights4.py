# Exerise 2.6 on page 57 of the textbook.

from numpy import zeros, double
import matplotlib.pyplot as plt

family1_heights = zeros(4, double);
family2_heights = zeros(4, double);
numbering_of_family_members = zeros(4, int);

family1_heights[0] = 1.60;
family1_heights[1] = 1.85;
family1_heights[2] = 1.75;
family1_heights[3] = 1.80;

family2_heights[0] = 0.50;
family2_heights[1] = 0.70;
family2_heights[2] = 1.90;
family2_heights[3] = 1.75;

numbering_of_family_members[0] = 1;
numbering_of_family_members[1] = 2;
numbering_of_family_members[2] = 3;
numbering_of_family_members[3] = 4;

plt.plot(numbering_of_family_members, family1_heights, 'ro', numbering_of_family_members,
         family2_heights, 'bo')
plt.xlabel("Family member number");
plt.ylabel("Height");
plt.legend(["Family A", "Family B"]);
plt.axis([0, 5, 0, 2]);
plt.show();
