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
root.right.left = Node(5)
root.right.right = Node(8)
root.right.left.left = Node(6)
root.right.left.right = Node(7)
root.right.right.left = Node(9)
root.right.right.right = Node(10)
print("Leaf nodes count:", countLeafNodes(root))
