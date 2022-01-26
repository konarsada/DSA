class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def sortedArrToBST(arr):
    if(len(arr) == 0):
        return
    
    else:
        mid = int(len(arr) / 2)
        
        root = Node(arr[mid])
        root.left = sortedArrToBST(arr[:mid])
        root.right = sortedArrToBST(arr[mid+1:])
        
        return root

def inorder(root):
    if(root is None):
        return
    
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def preorder(root):
    if(root is None):
        return
    
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrToBST(arr)
preorder(root)