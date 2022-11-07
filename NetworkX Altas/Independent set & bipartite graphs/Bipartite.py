import networkx as nx

Bipartite = nx.Graph()

Bipartite.add_nodes_from(["Bob", "Carl", "Diane", "Eve", "Frank", "George"], bipartite=0)
Bipartite.add_nodes_from(["George", "Frank", "Eve", "Diane", "Carl", "Bob"], bipartite=1)
Bipartite.add_edges_from([("Bob", "George"), ("Bob", "Frank"), ("Bob", "Eve")])

import pandas as pd

df = pd.DataFrame(index=["Bob", "Carl", "Diane", "Eve", "Frank", "George"],
                  columns=["Bob", "Carl", "Diane", "Eve", "Frank", "George"],
                  data=[
                      [0, 1, 1, 1, 1, 1],
                      [1, 0, 1, 1, 1, 1],
                      [1, 1, 0, 1, 1, 1],
                      [1, 1, 1, 0, 1, 1],
                      [1, 1, 1, 1, 0, 1],
                      [1, 1, 1, 1, 1, 0]
                  ])

print(df)


