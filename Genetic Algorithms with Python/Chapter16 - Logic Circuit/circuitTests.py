class Node:
    def __init__(self, createGate, indexA=None, indexB=None):
        self.CreateGate = createGate
        self.IndexA = indexA
        self.IndexB = indexB

    def nodes_to_circuit(self, nodes):
        for i, node in enumerate(nodes):
            inputA = circuit[node.IndexA] if node.IndexA is not None \
                                             and i > node.IndexA else None

            inputB = circuit[node.IndexB] if node.IndexB is not None \
                                             and i > node.IndexB else None

