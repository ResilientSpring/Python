class binaryTree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """The method for printing the content of the node's data,
        so that you can see what data the node stores."""
        return str(self.data)

    @staticmethod
    def traverse(tree):
        if tree.left != None:
            binaryTree.traverse(tree.left)
        if tree.right is not None:
            binaryTree.traverse(tree.right)

        print(tree.data)


tree = binaryTree("Root", None, None)
BranchA = binaryTree("Branch A", None, None)
BranchB = binaryTree("Branch B", None, None)
tree.left = BranchA
tree.right = BranchB

LeafC = binaryTree("Leaf C", None, None)
LeafD = binaryTree("Leaf D", None, None)
LeafE = binaryTree("Leaf E", None, None)
LeafF = binaryTree("Leaf F", None, None)

BranchA.left = LeafC
BranchA.right = LeafD
BranchB.left = LeafE
BranchB.right = LeafF
