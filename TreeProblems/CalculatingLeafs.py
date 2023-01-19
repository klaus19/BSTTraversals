class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def countLeafNodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return countLeafNodes(root.left) + countLeafNodes(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.right.right = Node(7)
print("Leaf nodes count:", countLeafNodes(root))

