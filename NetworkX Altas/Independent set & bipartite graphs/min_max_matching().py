import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph(incoming_graph_data=[(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)])

nx.draw(G=G, with_labels=True, node_color='y', node_size=800)

plt.show()

print(nx.maximal_matching(G=G))

print(nx.is_matching(G=G, matching={(2, 4), (3, 5)}))
print(nx.maximal_independent_set(G=G))

# Returns the minimum maximal matching of G.
# That is, out of all maximal matchings of the graph G, the smallest is returned.
print(nx.algorithms.approximation.min_maximal_matching(G=G))

# Reference:
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.matching.min_maximal_matching.html#networkx.algorithms.approximation.matching.min_maximal_matching
