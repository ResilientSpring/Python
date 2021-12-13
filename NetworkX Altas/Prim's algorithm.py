from networkx.algorithms import tree
import networkx as nx
import matplotlib.pyplot as plt

G = nx.cycle_graph(4)
G.add_edge(0, 3, weight=2)

nx.draw_planar(G=G, with_labels=True, node_color='g', node_size=800, font_size=14, width=0.8)

plt.show()

mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)

edgelist = list(mst)

print(sorted(sorted(e) for e in edgelist))

# Reference:
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_edges.html
