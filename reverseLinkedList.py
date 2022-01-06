class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # insert in the begining of LL
    def addFirst(self, num):
        node = Node(num)
        node.next = self.head
        self.head = node
    
    # insert in the end of LL
    def addLast(self, num):
        node = Node(num)
        
        cur = self.head
        # when one or more nodes exist
        if(cur):
            while(cur.next != None):
                cur = cur.next
            cur.next = node
            node.next = None
        # when first node is inserted
        else:
            node.next = cur
            self.head = node
    
    # display LL
    def printLL(self):
        cur = self.head
        while(cur):
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")
    
    # print reverse LL - recursive
    def printReverse(self, temp):
        if(temp):
            self.printReverse(temp.next)
            print(temp.data, end=" ")
    
    # reverse LL
    def reverseLL(self):
        prev = None
        cur = self.head
        
        while(cur):
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        
        self.head = prev

ll = LinkedList()

ll.addLast(11)
ll.addLast(12)
ll.addLast(13)
ll.addFirst(10)

ll.printLL()
ll.printReverse(ll.head)

ll.reverseLL()
ll.printLL()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        