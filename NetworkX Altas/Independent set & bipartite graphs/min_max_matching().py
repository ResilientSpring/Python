import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph(incoming_graph_data=[(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)])

nx.draw(G=G, with_labels=True, node_color='y', node_size=800)

plt.show()

print(nx.maximal_matching(G=G))

print(nx.is_matching(G=G, matching={(2, 4), (3, 5)}))
print(nx.maximal_independent_set(G=G))
print(nx.algorithms.min_weight_matching(G=G))
