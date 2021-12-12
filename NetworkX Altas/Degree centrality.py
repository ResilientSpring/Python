import matplotlib.pyplot as plt
import networkx as nx

graph = nx.Graph()

edge = [('0', '1', 2.02), ('0', '3', 4.45),
        ('0', '10', 6.2), ('1', '4', 1.7),
        ('4', '5', 3.28), ('5', '7', 4.28),
        ('1', '10', 5.8), ('5', '12', 3.3),
        ('10', '11', 1.67), ('11', '12', 2.16),
        ('9', '10', 2.32), ('3', '9', 5.02),
        ]

graph.add_weighted_edges_from(edge)

nx.draw_planar(G=graph, with_labels=True, node_color='y', node_size=800, font_size=14, width=0.8)

plt.show()

print(nx.algorithms.centrality.degree_centrality(G=graph))

# Further reading:
# 1. https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.degree_centrality.html#networkx.algorithms.centrality.degree_centrality
# 2. https://networkx.org/documentation/stable/reference/algorithms/centrality.html
