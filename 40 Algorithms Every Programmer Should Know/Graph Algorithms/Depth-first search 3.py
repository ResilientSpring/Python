# Acclimatizing the breadth-first search to the depth-first search
# by replacing queue with stack
def dfs(graph, start):
    visited = []  # This contains all the vertices that have been visited. Initially, it will be empty.
    visited.append(start)

    stack = graph[start] # This contains all the vertices that we have & want to visit in next iterations.

    # Check if there exists even a single element in the stack.
    while stack:
        # Pop the top node in the stack and chose that node as the current node of this iteration.
        node = stack.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]  # Use neighbors to represent the node's directly connected nodes.

            # Now, add the node's neighbours one by one to the stack.
            for neighbour in neighbours:
                if neighbour not in visited:  # To prevent graph[start] from being added again.
                    stack.append(neighbour)

    return visited


# Adjacency list
graph = {"Amin": ['Wasim', 'Nick', "Mike"],
         "Wasim": ['Amin', 'Imran'],
         "Nick": ['Amin'],
         "Mike": ['Amin'],
         'Imran': ['Wasim', 'Faras'],
         'Faras': ['Imran']
         }


print()
