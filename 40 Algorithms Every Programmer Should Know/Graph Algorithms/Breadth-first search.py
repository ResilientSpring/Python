

# Adjacency list
Graph = {"Amin": ["Wasim", "Nick", "Mike"],
         "Wasim": ["Imran", "Amin"],
         "Nick": "Amin",
         "Mike": "Amin",
         "Imran": ["Wasim", "Faras"],
         "Faras": "Imran"
         }

def bfs(graph, start):
    visited = []  # This contains all the vertices that have been visited. Initially, it will be empty.
    queue = [start]  # This contains all the vertices that we have want to visit in next iterations.


    # Pop the first node from the queue and chose that node as the current node.
    node = queue.pop(0)


