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

def parentNode(root, data, parent=None):
        if(root is None):
            return
        
        if(data < root.data):
            return parentNode(root.left, data, root)
        
        elif(data > root.data):
            return parentNode(root.right, data, root)
        
        else:
            return parent

def deleteNode(root, data):
    global r
    
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
            parent = parentNode(r, data)
            
            if(data < parent.data):
                parent.left = None
            else:
                parent.right = None
        
        # if only one child
        elif(root.left is None):
            parent = parentNode(r, data)
            
            if(data < parent.data):
                parent.left = root.right
            else:
                parent.right = root.right
        
        elif(root.right is None):
            parent = parentNode(r, data)
            
            if(data < parent.data):
                parent.left = root.left
            else:
                parent.right = root.left
        
        # if both child
        else:
            inPred = maxValueNode(root)
            
            parent = parentNode(r, inPred.data)
            if(inPred.data < parent.data):
                parent.left = None
            else:
                parent.right = None
            
            root.data = inPred.data
            
            

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

deleteNode(r, 30)
inorder(r)
print()