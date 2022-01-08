class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def nLast(self, n):
        front = self.head
        back = self.head
        
        temp = n - 1
        while(temp):
            front = front.next
            temp -= 1
        
        while(front):
            front = front.next
            back = back.next
        
        return back.data

ll = LinkedList()

ll.push(20)
ll.push(4)
ll.push(15)
ll.push(35)

print(ll.nLast(3))