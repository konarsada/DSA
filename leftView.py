class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def height(node):
    if(node is None):
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        
        if(lheight > rheight):
            return lheight + 1
        else:
            return rheight + 1

def leftView(root):
    global arr
    
    h = height(root)
    arr = [False] * h
    
    for i in range(h):
        printLeftView(root, i, i)

def printLeftView(node, level, height):
    global arr
    
    if(node is None):
        return
    
    if(level == 0 and arr[height] == False):
        arr[height] = True
        print(node.data)
    
    elif(level > 0):
        printLeftView(node.left, level-1, height)
        printLeftView(node.right, level-1, height)

arr = []

root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)

leftView(root)