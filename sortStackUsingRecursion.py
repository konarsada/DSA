def reverse():
    if(len(stack) > 0):
        item = stack.pop()
        reverse()
        insertAtBack(item)

def insertAtBack(x):
    if(len(stack) == 0):
        stack.append(x)
    
    else:
        y = stack.pop()
        insertAtBack(x)
        stack.append(y)
        

stack = ['a', 'b', 'c', 'd']

print(stack)

reverse()

print(stack)