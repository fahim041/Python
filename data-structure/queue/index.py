class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        if not self.first:
            return
        temp = self.first
        self.first = temp.next
        temp.next = None


queue = Queue(4)
queue.enqueue(7)
queue.enqueue(10)
queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.enqueue(11)
queue.enqueue(12)
queue.dequeue()
queue.print_queue()
