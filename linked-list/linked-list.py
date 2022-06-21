class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        print("Printing linkedlist...")
        if self.length == 0:
            print('list is empty')
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        print("removing node with value ", temp.value)
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def bubbleSort_value(self):
        end = None
        
        while end != self.head.next:
            p = self.head
            while p.next != end:
                q = p.next
                if p.value > q.value:
                    p.value, q.value = q.value, p.value
                p = p.next
            end = p


linked_list = LinkedList(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(28)
linked_list.append(45)
linked_list.append(3)

# linked_list.pop()

# linked_list.print_list()

linked_list.prepend(10)
linked_list.prepend(11)

linked_list.popfirst()

print(linked_list.get(2))
linked_list.set_value(2, 99)

linked_list.print_list()

linked_list.bubbleSort_value()

linked_list.print_list()
