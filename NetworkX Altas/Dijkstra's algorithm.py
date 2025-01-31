import matplotlib.pyplot as plt
import networkx as nx

graph = nx.Graph()

edge = [('a', 'b', 0.3), ('b', 'c', 0.9), ('a', 'c', 0.5), ('c', 'd', 1.2)]

graph.add_weighted_edges_from(edge)

nx.draw(graph)

plt.show()
