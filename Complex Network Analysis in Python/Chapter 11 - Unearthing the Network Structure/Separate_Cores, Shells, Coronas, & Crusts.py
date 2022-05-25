import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph((("Alpha", "Brazo"), ("Brazo", "Charlie"), ("Charlie", "Delta"), ("Charlie", "Echo"),
              ("Charlie", "Foxtrot"), ("Delta", "Echo"), ("Delta", "Foxtrot"), ("Echo", "Foxtrot"),
              ()))
