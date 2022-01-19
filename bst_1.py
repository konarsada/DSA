class RootNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder(root):
    if(root is None):
        return
    
    else:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def insertNode(root, data):    
    if(data < root.data):
        if(root.left is None):
            root.left = RootNode(data)
        else:
            insertNode(root.left, data)
    
    elif(data > root.data):
        if(root.right is None):
            root.right = RootNode(data)
        else:
            insertNode(root.right, data)
    
def maxValueNode(node):
    node = node.left
    while(node.right is not None):
        node = node.right
    
    return node

def deleteNode(root, data):
    if(root is None):
        return
    
    if(data < root.data):
        deleteNode(root.left, data)
    
    elif(data > root.data):
        deleteNode(root.right, data)
    
    # when equal
    else:
        # if leaf node
        if(root.left is None and root.right is None):
            root.data = None
        
        # if only one child
        elif(root.left is None):
            root.data = root.right.data
            root.right = None
        
        elif(root.right is None):
            root.data = root.left.data
            root.left = None
        
        # if both child
        else:
            inPred = maxValueNode(root)
            root.data = inPred.data
            deleteNode(root.left, root.data)
            

r = RootNode(50)
insertNode(r, 30)
insertNode(r, 20)
insertNode(r, 40)
insertNode(r, 70)
insertNode(r, 60)
insertNode(r, 80)
insertNode(r, 55)

inorder(r)
print()

deleteNode(r, 60)
inorder(r)
print()

deleteNode(r, 55)
inorder(r)
print()