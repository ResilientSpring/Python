import networkx as nx
import matplotlib.pyplot as plt

triangle_graph = nx.from_edgelist([(1, 2), (2, 3), (3, 1)], create_using=nx.DiGraph)
nx.draw_planar(triangle_graph, with_labels=True, node_size=1000, node_color="#ffff8f",
               width=0.8, font_size=14)

plt.show()

# Reference: https://networkx.org/nx-guides/content/algorithms/dag/index.html
