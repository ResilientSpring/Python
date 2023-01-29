def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for next in graph[start] - visited:
        dfs(graph=graph, start=next, visited=visited)

    return visited


graph = {"Amin": ['Wasim', 'Nick', "Mike"]}
