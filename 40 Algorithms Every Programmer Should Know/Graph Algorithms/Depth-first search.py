def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for next in graph[start] - visited:
        dfs(graph=graph, start=next, visited=visited)

    return visited


# Adjacency list
graph = {"Amin": ['Wasim', 'Nick', "Mike"],
         "Wasim": ['Amin', 'Imran'],
         "Nick": ['Amin'],
         "Mike": ['Amin'],
         'Imran': ['Wasim', 'Faras'],
         'Faras': ['Imran']
         }
