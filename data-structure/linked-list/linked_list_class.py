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
        print("Printing linked list...")
        if self.length == 0:
            print('list is empty')
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def get_length(self):
        if self.head is None:
            return 0
        temp = self.head
        counter = 0
        while temp:
            counter += 1
            temp = temp.next
        return counter

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
        return temp

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

    def pop_first(self):
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

    def get_index(self, value):
        if self.length == 0:
            return -1
        if self.head.value == value:
            return 0
        temp = self.head
        counter = 0
        while temp:
            counter += 1
            if temp.value == value:
                return counter - 1
            temp = temp.next
        return -1

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        temp = self.head
        pre = None
        for _ in range(index):
            pre = temp
            temp = temp.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head, self.tail = self.tail, self.head
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def copy_list(self):
        new_list = LinkedList(self.head.value)
        temp = self.head.next
        while temp:
            new_list.append(temp.value)
            temp = temp.next
        return new_list

    def bubble_sort(self):
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

linked_list.pop()

linked_list.print_list()
