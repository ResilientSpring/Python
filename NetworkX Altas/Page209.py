import networkx as nx
import matplotlib.pyplot as plt

vertices = ['A', 'B', 'C', 'D', 'E']

edges = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('E', 'D'), ('D', 'C')]

directed_graph = nx.DiGraph()

directed_graph.add_nodes_from(vertices)
directed_graph.add_edges_from(edges)

nx.draw(G=directed_graph)

nx.draw_planar(G=directed_graph)

plt.show()
