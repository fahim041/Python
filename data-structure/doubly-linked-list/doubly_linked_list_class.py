class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        current = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = current.prev
            self.tail.next = None
            current.prev = None
        self.length -= 1
        return current


doubly_linked_list = DoublyLinkedList(7)
doubly_linked_list.append(4)
doubly_linked_list.append(6)

doubly_linked_list.pop()
doubly_linked_list.pop()
doubly_linked_list.pop()


doubly_linked_list.print_list()
