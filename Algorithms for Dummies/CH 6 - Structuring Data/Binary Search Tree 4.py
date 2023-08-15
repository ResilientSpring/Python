class binaryTree:

    # Constructor
    def __init__(self, nodeData, left=None, right=None):
        self.nodeData = nodeData
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.nodeData)


# root_node = binaryTree("Root", left=branch_A, right=branch_B)

leaf_C = binaryTree(nodeData="Leaf C", left=None, right=None)
leaf_D = binaryTree(nodeData="Leaf D", left=None, right=None)

branch_A = binaryTree(nodeData="Branch A", left=leaf_C, right=leaf_D)

leaf_E = binaryTree(nodeData="Leaf E", left=None, right=None)
leaf_F = binaryTree(nodeData="Leaf F", left=None, right=None)

branch_B = binaryTree(nodeData="Branch B", left=leaf_E, right=leaf_F)

root_node = binaryTree("Root", left=branch_A, right=branch_B)

def traverse(tree):
    if tree.left is not None:
        traverse(tree.left)
    if tree.right is not None:
        traverse(tree.right)

    print(tree.nodeData)


traverse(root_node)
