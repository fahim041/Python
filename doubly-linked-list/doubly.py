from email.errors import NonPrintableDefect
from django.forms import SelectDateWidget


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def appendFirst(self, value):
        new_node = Node(value)
        if not self.head:
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return True

    def pop(self):
        if not self.head:
            return None
        if not self.head.next:
            self.head = None
            self.tail = None
            return
        temp = self.tail
        self.tail = temp.prev
        temp.prev = None
        self.tail.next = None
        return temp

    def display(self, type):
        if type == 'ltr':
            temp = self.head
            while temp:
                print(temp.data, end='-> ')
                temp = temp.next
            print()
        else:
            temp = self.tail
            while temp:
                print(temp.data, end='-> ')
                temp = temp.prev
            print()

d = DoublyLinkedList()

d.append(3)
d.append(4)
d.append(6)
d.append(5)
d.append(10)

d.appendFirst(99)
d.appendFirst(88)

d.display('rtl')