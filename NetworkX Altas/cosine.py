import math

import matplotlib.pyplot as plt
import networkx as nx

graph = nx.Graph()

graph.add_edge('y', 'x', function=math.cos)
graph.add_node(math.cos)

nx.draw_planar(G=graph)

plt.show()
