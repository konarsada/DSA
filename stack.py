'''
Array implementation of stack

stack = [20, 11, 15, 13, 18, 9]
print(stack)

# push
stack.append(3)
print("push", stack)

# pop
item = stack.pop()
print("pop", item, stack)

# peek
item = stack[len(stack)-1]
print("peek", item, stack)

'''

# Linked list implementation of stack

# Class Node

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    # Head
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if(self.head is None):
            return True
        return False
    
    # head points to new node
    def push(self, data):
        item = StackNode(data)
        item.next = self.head
        self.head = item
        print("pushed", data)
        return
    
    # delete head
    def pop(self):
        if(self.isEmpty()):
            print("stack empty")
            return
        item = self.head.data
        self.head = self.head.next
        print("popped", item)
        return
    
    # print root node
    def peek(self):
        if(self.isEmpty()):
            print("stack empty")
            return
        print("peek", self.head.data)
        return

stack = Stack()
stack.push(10)
stack.peek()
stack.pop()
stack.peek()
stack.pop()
stack.push(10)
stack.push(100)
stack.push(11)
stack.pop()
stack.peek()