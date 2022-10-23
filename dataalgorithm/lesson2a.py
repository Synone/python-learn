class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)


list1 = LinkedList()
list1.head = Node(4)
list1.head.next = Node(3)
list1.head.next.next = Node(4)
print(list1.head.data, list1.head.next.data, list1.head.next.next.data)

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)