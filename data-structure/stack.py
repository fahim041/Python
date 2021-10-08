class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def top(self):
        return self.items[0]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            print("No element in the stack")

    def size(self):
        return len(self.items)

    def printStack(self):
        print(self.items)


s = Stack()
s.push("a")
s.push("b")
s.push("c")
s.printStack()
s.pop()
s.pop()
s.printStack()
