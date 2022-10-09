class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end='-> ')
            temp = temp.next
        print('\n')

    def getCount(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next

        return count

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return 

        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node

    def pop(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None
        print('temp', temp.data)
        return temp

    def deleteNode(self, value):
        temp = self.head
        if temp:
            if temp.data == value:
                self.head = temp.next
                temp = None
                return
        while temp:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        
        if(temp == None):
            return
        
        prev.next = temp.next
        temp = None
        
    def get_index(self, value):
        temp = self.head
        index = 0
        while temp:
            if temp.data == value:
                break
            index += 1
            temp = temp.next
        return index

    def insertIndex(self, index, value):
        new_node = Node(value)
        temp = self.head
        for _ in range(index):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        return True

    def reverse(self):
        prev, temp = None, self.head

        while temp:
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after

        self.head = prev

l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.append(8)
l.append(9)

l.printList()

l.reverse()

l.printList()

