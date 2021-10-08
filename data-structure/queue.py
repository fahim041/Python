class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def top(self):
        return self.items[0]

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if len(self.items) != 0:
            return self.items.pop(0)
        else:
            print("No element in the stack")

    def size(self):
        return len(self.items)

    def printQueue(self):
        print(self.items)

q = Queue()
q.enqueue("Test")
q.enqueue("Unit")
q.printQueue()

q.dequeue()

q.printQueue()