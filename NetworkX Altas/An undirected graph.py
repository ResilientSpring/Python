import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1, 13)

edges = [(2, 8), (2, 3), (2, 6), (3, 0), (3, 9), (0, 1), (0, 10), (9, 10), (1, 4), (10, 11), (4, 5),
         (11, 12), (12, 5), (5, 7)]

directed_acyclic_graph = nx.Graph()
directed_acyclic_graph.add_nodes_from(vertices)
directed_acyclic_graph.add_edges_from(edges)

nx.draw(G=directed_acyclic_graph)

plt.show()
