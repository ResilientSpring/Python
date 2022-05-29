import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(n=4)

nx.draw(G=G, with_labels=True, node_color='y', node_size=800)

plt.show()

print(nx.predecessor(G=G, source=0, target=3))
