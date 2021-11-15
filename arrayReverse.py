
def reverseListFunction(myList, start, end):
    if(start >= end):
        return
    else:
        myList[start], myList[end] = myList[end], myList[start]
        reverseListFunction(myList, start+1, end-1)

myList = list(range(5))
print("list is", myList)
reverseListFunction(myList, 0, len(myList)-1)
print("reverse list is", myList)