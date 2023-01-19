class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_depth(root):
    if root is None:
        return 0
    left_depth = find_depth(root.left)
    right_depth = find_depth(root.right)
    return max(left_depth, right_depth) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Depth of the tree:", find_depth(root))   # output will be 3
