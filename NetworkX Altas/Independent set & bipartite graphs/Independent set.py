import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(n=5)

nx.draw(G=G, with_labels=True, node_color='y', node_size=800)

plt.show()

print(nx.maximal_independent_set(G=G))
print(nx.maximal_independent_set(G=G))
print(nx.maximal_independent_set(G=G))
print(nx.maximal_independent_set(G=G, nodes=[1]))
print(nx.maximal_independent_set(G=G, nodes=[4]))

# Reference:
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.mis.maximal_independent_set.html#networkx.algorithms.mis.maximal_independent_set
