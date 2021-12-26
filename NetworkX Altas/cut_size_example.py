import networkx as nx
import matplotlib.pyplot as plt

graph = nx.barbell_graph(m1=3, m2=0)

nx.draw_planar(G=graph, with_labels=True, node_color='g', node_size=800, font_size=14, width=0.8)

plt.show()

print(nx.algorithms.is_directed_acyclic_graph(graph))

print(nx.cut_size(graph, {0, 1, 2}, {3, 4, 5}))

# Reference:
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.cuts.cut_size.html#networkx.algorithms.cuts.cut_size
