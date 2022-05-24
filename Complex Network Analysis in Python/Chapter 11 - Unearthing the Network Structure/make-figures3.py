import networkx as nx
import matplotlib.pyplot as plt
import random
random.seed(246)
import numpy as np
np.random.seed(4812)

F = nx.DiGraph()
F.add_node("C")

F.add_edges_from([("B", "b0"), ("b0", "b1"), ("b1", "B")])
F.add_edges_from([("A", "a0"), ("a0", "a1"), ("a1", "a2"), ("a1", "a3"), ("a3", "A")])

nx.draw_networkx(G=F, arrows=True, with_labels=True)

plt.show()

print(nx.strongly_connected_components(G=F))
