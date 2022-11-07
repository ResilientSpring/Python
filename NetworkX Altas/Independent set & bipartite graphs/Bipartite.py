import networkx as nx

Bipartite = nx.Graph()

Bipartite.add_nodes_from(["Bob", "Carl", "Diane", "Eve", "Frank", "George"], bipartite=0)
Bipartite.add_nodes_from(["George", "Frank", "Eve", "Diane", "Carl", "Bob"], bipartite=1)
Bipartite.add_edges_from([("Bob", "George"), ("Bob", "Frank"), ("Bob", "Eve")])

# Abandoned because this method is overly time-consuming.

# Reference: https://stackoverflow.com/a/62519225/
