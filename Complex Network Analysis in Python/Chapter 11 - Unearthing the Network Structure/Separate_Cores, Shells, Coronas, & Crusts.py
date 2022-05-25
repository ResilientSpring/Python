import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

random.seed(5)
np.random.seed(15)

G = nx.Graph((("Alpha", "Brazo"), ("Brazo", "Charlie"), ("Charlie", "Delta"), ("Charlie", "Echo"),
              ("Charlie", "Foxtrot"), ("Delta", "Echo"), ("Delta", "Foxtrot"), ("Echo", "Foxtrot"),
              ("Echo", "Golf"), ("Echo", "Hotel"), ("Foxtrot", "Golf"), ("Foxtrot", "Hotel"),
              ("Delta", "Hotel"), ("Golf", "Hotel"), ("Delta", "India"), ("Charlie", "India"),
              ("India", "Juliet"), ("Golf", "Kilo"), ("Alpha", "Kilo"), ("Bravo", "Lima")))

nx.draw_networkx(G=G, arrows=True, with_labels=True)

plt.show()

print(nx.k_core(G=G).nodes())
print(nx.k_crust(G=G).nodes())
