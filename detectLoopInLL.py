'''
# time- O(n): One traversal of loop
# space- O(n): store values in hashmap
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
    
    def detectLoop(self):
        my_hash = {}
        
        temp = self.head
        while(temp):
            if(temp.data in my_hash):
                return True
            
            my_hash[temp.data] = temp.data
            temp = temp.next
        
        return False
'''

# time- O(n): One traversal of loop
# space- O(1): No extra space
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        self.flag = 0

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def detectLoop(self):
        temp = self.head
        
        while(temp):
            if(temp.flag == 1):
                return True
            
            temp.flag = 1
            
            temp = temp.next
        
        return False

ll = LinkedList()
ll.push(20)
ll.push(4)
ll.push(15)
ll.push(10)

# create a loop
ll.head.next.next.next.next = ll.head

if(ll.detectLoop()):
    print("Loop present")
else:
    print("Loop not present")








































