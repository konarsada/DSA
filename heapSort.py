def maxHeapify(arr, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    
    if(l < len(arr) and arr[l] > arr[largest]):
        largest = l
    
    if(r < len(arr) and arr[r] > arr[largest]):
        largest = r
    
    if(largest != i):
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest)

def buildMaxHeap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        maxHeapify(arr, i)

def heapSort(arr):
    buildMaxHeap(arr)
    
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxHeapify(arr, 0)

arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
print(arr)
heapSort(arr)
print(arr)