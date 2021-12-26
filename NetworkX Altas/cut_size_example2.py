import networkx as nx
import matplotlib.pyplot as plt

graph = nx.MultiGraph(["ab", "ab"])
S = {"a"}
T = {"b"}

nx.draw_planar(G=graph, with_labels=True, node_color='g', node_size=800, font_size=14, width=0.8)

plt.show()

print(nx.cut_size(graph, {"a"}, {"b"}))
