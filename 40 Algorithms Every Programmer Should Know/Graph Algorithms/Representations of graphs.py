import networkx as nx

graph = nx.Graph()

# Add a single vertex
graph.add_node("Mike")

# Add a bunch of vertices using a list
graph.add_nodes_from(["Amine", "Wassim", "Nick"])

# Add an edge between the existing vertices.
graph.add_edge("Mike", "Amine")

# Print the edges and vertices.
print(graph.edges)
print(graph.nodes)

# If we are adding an edge, this also leads to adding the associated vertices,
# if they do not already exist
graph.add_edge("Amine", "Imran")

print(graph.nodes)
print(graph.edges)

