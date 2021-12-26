import networkx as nx
import matplotlib.pyplot as plt

graph = nx.barbell_graph(m1=3, m2=0)

nx.draw_planar(G=graph, with_labels=True, node_color='g', node_size=800, font_size=14, width=0.8)

plt.show()

print(nx.algorithms.is_directed_acyclic_graph(graph))
