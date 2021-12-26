import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.approximation as approximate


def circuit_to_formula(circuit):
    # Convert the circuit to an equivalent formula.
    formula = nx.dag_to_branching(circuit)
    # Transfer the operator or variable labels for each node from the
    # circuit to the formula.
    for v in formula:
        source = formula.nodes[v]["source"]
        formula.nodes[v]["label"] = circuit.nodes[source]["label"]
    return formula


def formula_to_string(formula):
    def _to_string(formula, root):
        # If there are no children, this is a variable node.
        label = formula.nodes[root]["label"]
        if not formula[root]:
            return label
        # Otherwise, this is an operator.
        children = formula[root]
        # If one child, the label must be a NOT operator.
        if len(children) == 1:
            child = nx.utils.arbitrary_element(children)
            return f"{label}({_to_string(formula, child)})"
        # NB "left" and "right" here are a little misleading: there is
        # no order on the children of a node. That's okay because the
        # Boolean AND and OR operators are symmetric. It just means that
        # the order of the operands cannot be predicted and hence the
        # function does not necessarily behave the same way on every
        # invocation.
        left, right = formula[root]
        left_subformula = _to_string(formula, left)
        right_subformula = _to_string(formula, right)
        return f"({left_subformula} {label} {right_subformula})"

    root = next(v for v, d in formula.in_degree() if d == 0)
    return _to_string(formula, root)


circuit = nx.DiGraph()
# Layer 0
circuit.add_node(0, label="PI1", layer=0)
circuit.add_node(1, label="PI2", layer=0)
circuit.add_node(2, label="PI3", layer=0)
circuit.add_node(3, label="PI4", layer=0)
circuit.add_node(4, label="PI5", layer=0)

# Layer 1
circuit.add_node(5, label="A", layer=1)
circuit.add_node(6, label="B", layer=1)
circuit.add_node(7, label="C", layer=1)
circuit.add_node(8, label="D", layer=1)

circuit.add_edge(0, 5)
circuit.add_edge(1, 5)
circuit.add_edge(1, 6)
circuit.add_edge(2, 6)
circuit.add_edge(2, 7)
circuit.add_edge(3, 7)
circuit.add_edge(3, 8)
circuit.add_edge(4, 8)

# Layer 2
circuit.add_node(9, label="E", layer=2)
circuit.add_node(10, label="F", layer=2)
circuit.add_node(11, label="G", layer=2)
circuit.add_node(12, label="H", layer=2)

circuit.add_edge(4, 12)

circuit.add_edge(5, 9)
circuit.add_edge(6, 9)
circuit.add_edge(6, 10)
circuit.add_edge(7, 10)
circuit.add_edge(7, 11)
circuit.add_edge(8, 11)

# Layer 3
circuit.add_node(13, label="I", layer=3)
circuit.add_node(14, label="PO1", layer=3)

# Layer 4
circuit.add_node(15, label="PO2", layer=4)


circuit.add_edge(9, 15)
circuit.add_edge(10, 13)
circuit.add_edge(11, 13)
circuit.add_edge(11, 14)
circuit.add_edge(12, 14)

circuit.add_edge(13, 15)

# Convert the circuit to an equivalent formula.
formula = circuit_to_formula(circuit)
print(formula_to_string(formula))

labels = nx.get_node_attributes(circuit, "label")

options = {
    "node_size": 600,
    "alpha": 0.5,
    "node_color": "blue",
    "labels": labels,
    "font_size": 22,
}

plt.figure(figsize=(8, 8))
pos = nx.multipartite_layout(circuit, subset_key="layer")
nx.draw_networkx(circuit, pos, **options)
plt.title(formula_to_string(formula))
plt.axis("equal")
plt.show()

print(nx.algorithms.tree.is_tree(G=circuit))
print(nx.algorithms.tree.is_forest(G=circuit))

residential = nx.algorithms.cut_size(G=circuit, S={i for i in range(1, 6)}, T={j for j in range(14, 16)})

print(residential)

print(nx.algorithms.is_directed_acyclic_graph(G=circuit))
