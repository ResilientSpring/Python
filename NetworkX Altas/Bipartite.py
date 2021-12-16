from networkx.algorithms import bipartite
import networkx as nx
import matplotlib.pyplot as plt

B = nx.Graph()

# Add nodes with the node attribute "bipartite"
B.add_nodes_from([1, 2, 3, 4], bipartite=0)
B.add_nodes_from(["a", "b", "c"], bipartite=1)

# Add edges only between nodes of opposite node sets
B.add_edges_from([(1, "a"), (1, "b"), (2, "b"), (2, "c"), (3, "c"), (4, "a")])

c = bipartite.color(G=B)
print(c)

nx.draw_planar(G=B, with_labels=True, node_color='g', node_size=800, font_size=14, width=0.8)

plt.show()
