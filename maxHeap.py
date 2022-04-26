def maxHeapify(arr, i):
    l = 2 * i + 1
    r = 2 * i + 2
    
    largest = i
    
    if(l < len(arr) and arr[l] > arr[largest]):
        largest = l
    
    if(r < len(arr) and arr[r] > arr[largest]):
        largest = r
    
    if(i != largest):
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest)

def buildMaxHeap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        maxHeapify(arr, i)

# arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
arr = [7, 10, 4, 3, 20, 15]
print(arr)
buildMaxHeap(arr)
print(arr)