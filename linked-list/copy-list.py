class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
def print_list(head):
    temp = head
    while temp:
        print(temp.value)
        temp = temp.next
        
def copy_list(head):
    if head is None:
        return None
    newNode = Node(head.value)
    newNode.next = copy_list(head.next)
    
    return newNode
        
head = None
for i in reversed(range(4)):
    head = Node(i+1, head)
    
duplicate_list = copy_list(head)
print_list(duplicate_list)