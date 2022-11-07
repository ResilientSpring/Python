import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.DataFrame(index=["Bob", "Carl", "Diane", "Eve", "Frank", "George"],
                  columns=["Bob1", "Carl1", "Diane1", "Eve1", "Frank1", "George1"],
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
Bipartite.add_nodes_from(df.index, bipartite=0)
Bipartite.add_nodes_from(df.columns, bipartite=1)

s = df.stack()
Bipartite.add_edges_from(s[s == 1].index)

top = nx.bipartite.sets(G=Bipartite)[0]
pos = nx.bipartite_layout(G=Bipartite, nodes=top)

nx.draw(Bipartite, pos=pos, node_color='lightgreen', node_size=2500, with_labels=True)

plt.show()
