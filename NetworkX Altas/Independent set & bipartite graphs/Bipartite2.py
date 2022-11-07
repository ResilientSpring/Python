import pandas as pd
import networkx as nx

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


Bipartite = nx.Graph()
