import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(n=5)

nx.draw(G=G, with_labels=True, node_color='y', node_size=800)

plt.show()

print(nx.maximal_independent_set(G=G))
print(nx.maximal_independent_set(G=G))
