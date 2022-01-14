# Level Order Traversal = BFS

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
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

def printLevelOrder(root):
    h = height(root)
    
    for i in range(1, h+1):
        printCurrentLevel(root, i)

def printCurrentLevel(node, level):
    if(node is None):
        return
    if(level == 1):
        print(node.data, end=" ")
    elif(level > 1):
        printCurrentLevel(node.left, level-1)
        printCurrentLevel(node.right, level-1)
'''

def printLevelOrder(root):
    if(root is None):
        return
    
    q = []
    
    q.append(root)
    
    while(q):
        item = q.pop(0)
        print(item.data, end=" ")
        
        if(item.left is not None):
            q.append(item.left)
        
        if(item.right is not None):
            q.append(item.right)

def printPostOrder(root):
    if(root is None):
        return
    else:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.data, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order or BFS", end=": ")
printLevelOrder(root)

print("Postorder", end=": ")
printPostOrder(root)