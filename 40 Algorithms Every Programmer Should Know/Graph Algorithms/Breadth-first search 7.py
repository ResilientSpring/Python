

# Adjacency list
Graph = {"Amin": ["Wasim", "Nick", "Mike"],
         "Wasim": ["Imran", "Amin"],
         "Nick": "Amin",
         "Mike": "Amin",
         "Imran": ["Wasim", "Faras"],
         "Faras": "Imran"
         }

print(Graph["Amin"])

def bfs(graph, start):
    visited = []  # This contains all the vertices that have been visited. Initially, it will be empty.
    visited.append(start)

    queue = graph[start]  # This contains all the vertices that we have want to visit in next iterations.

    # Check if there exists even a single element in the queue.
    while queue:
        # Pop the first node from the queue and chose that node as the current node of this iteration.
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]  # Use neighbors to represent the node's directly connected nodes.

            # Now, add the node's neighbours one by one to the queue.
            for neighbour in neighbours:
                if neighbour not in visited:  # To prevent graph[start] from being added again.
                    queue.append(neighbour)

    return visited


bfs(graph=Graph, start="Amin")
