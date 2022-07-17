import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edge('p', 'y', capacity=5.0)
G.add_edge('p', 's', capacity=4.0)
G.add_edge('y', 't', capacity=3.0)
G.add_edge('s', 'h', capacity=5.0)
G.add_edge('s', 'o', capacity=4.0)

flow_value = nx.maximum_flow_value(flowG=G, _s='p', _t='o')

print("Flow value", flow_value)

nx.draw(G=G, node_color='#a0cbe2')

plt.show()
