from collections import deque
from os import curdir


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True

        current = self.root
        while True:
            if new_node.value == current.value:
                return False
            if new_node.value < current.value:
                if not current.left:
                    current.left = new_node
                    return True
                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    return True
                current = current.right

    def find(self, value):
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    def inorder(self):
        self.__inorder(self.root)

    def preorder(self):
        self.__preorder(self.root)

    def __inorder(self, root):
        if root:
            self.__inorder(root.left)
            print(root.value, end='->')
            self.__inorder(root.right)
            print('end')

    def __preorder(self, root):
        if root:
            print(root.value, end='->')
            self.__preorder(root.left)
            self.__preorder(root.right)


def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1


def depth(root):
    level = 0
    queue = deque()
    queue.append(root)
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return level


def findMax(root):
    if not root:
        return float('-inf')
    res = root.value
    lres = findMax(root.left)
    rres = findMax(root.right)
    if (lres > res):
        res = lres
    if (rres > res):
        res = rres
    return res


def findMin(root):
    if not root:
        return float('inf')
    res = root.value
    lres = findMin(root.left)
    rres = findMin(root.right)
    if (lres < res):
        res = lres
    if (rres < res):
        res = rres
    return res


bst = Tree()
bst.insert(3)
bst.insert(2)
bst.insert(9)
bst.insert(7)
bst.insert(20)


print(findMax(bst.root))
