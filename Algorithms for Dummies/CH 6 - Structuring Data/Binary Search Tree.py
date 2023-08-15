class binaryTree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """The method for printing the content of the node's data,
        so that you can see what data the node stores."""
        return str(self.data)


tree = binaryTree("Root", None, None)
BranchA = binaryTree("Branch A", None, None)
BranchB = binaryTree("Branch B", None, None)

