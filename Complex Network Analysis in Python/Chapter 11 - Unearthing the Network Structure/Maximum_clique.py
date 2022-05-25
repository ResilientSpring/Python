import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

random.seed(1)
np.random.seed(2)

# Generate a 5-clique
G = nx.complete_graph(n=5, create_using=nx.Graph())

nx.relabel_nodes(G=G, mapping=dict(enumerate(("Alpha", "Bravo", "Charlie", "Delta", "Echo"))), copy=False)

# Attach a pigtail to it
G.add_edges_from([("Echo", "Foxtrot"), ("Foxtrot", "Golf"), ("Foxtrot", "Hotel"), ("Golf", "Hotel")])

nx.draw_networkx(G=G, arrows=True, with_labels=True)

plt.show()
