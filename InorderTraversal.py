class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data, end=' ')
        in_order_traversal(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

in_order_traversal(root)   # this is the output that I am receiving :-  4 2 5 1 3 None
