class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = 0


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return
        temp = self.top
        self.top = temp.next
        temp.next = None


stack = Stack(4)
stack.push(6)
stack.push(7)

stack.pop()
stack.pop()
stack.pop()

stack.push(11)
stack.push(22)
stack.pop()
stack.print_stack()
