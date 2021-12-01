import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1, 10)

edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]

graph = nx.Graph()
graph.add_nodes_from(vertices)
graph.add_edges_from(edges)

nx.draw(graph, with_labels=True, node_color='y', node_size=800)

plt.show()
