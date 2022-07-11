class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def print_list(head):
    current = head
    while current:
        print(current.value, end='-->')
        current = current.next
    print('None')

def push(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node

def constructList(keys):
    dummy = Node()
    tail = dummy

    print('print -> next', tail.next)

    tail.next = push(tail.next, keys)
    tail = tail.next

    print_list(tail)

    print_list(dummy.next)

    return dummy.next


def reverse(head):
    current = head
    previous = None
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


head = None
for i in reversed(range(6)):
    head = Node(i + 1, head)
print_list(head)

first_node = push(head, 55)


constructList(1)
