class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end='->')
        inorder(root.right)


def insert(node, value):
    if node is None:
        return Node(value)

    if node.value == value:
        return node
    elif value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    return node


bst = BST()
bst.insert(4)
bst.insert(10)
bst.insert(22)
bst.insert(1)
bst.insert(11)

inorder(bst.root)

# root = None
# root = insert(root, 4)
# root = insert(root, 10)
# root = insert(root, 22)
# root = insert(root, 1)
# root = insert(root, 11)
# root = insert(root, 10)

# inorder(root)
