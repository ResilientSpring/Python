import matplotlib.pyplot as plt
import networkx as nx

graph = nx.Graph()

edge = [('a', 'b', 0.3), ('b', 'c', 0.9), ('a', 'c', 0.5), ('c', 'd', 1.2)]

graph.add_weighted_edges_from(edge)

nx.draw_planar(G=graph, with_labels=True, node_color='y', node_size=800, font_size=14, width=0.8)

plt.show()

print(nx.dijkstra_path(G=graph, source='a', target='d'))

# Reference:
# 1.https://networkx.org/documentation/stable/reference/introduction.html#algorithms
