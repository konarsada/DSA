def maxHeapify(arr, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    
    largest = i
    
    if(l < n and arr[l] > arr[largest]):
        largest = l
    if(r < n and arr[r] > arr[largest]):
        largest = r
    
    if(largest != i):
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest, n)

def buildMaxHeap(arr):
    heapSize = len(arr)
    for i in range(heapSize // 2 - 1, -1, -1):
        maxHeapify(arr, i, heapSize)

def getKthMax(arr, k):
    buildMaxHeap(arr)
    
    heapSize = len(arr)
    countK = 0
    
    for i in range(len(arr) - 1, 0, -1):
        countK += 1
        if(countK == k):
            return arr[0]
        arr[i], arr[0] = arr[0], arr[i]
        heapSize -= 1
        maxHeapify(arr, 0, heapSize)

arr = [7, 10, 4, 3, 20, 15]
print(arr)
print(getKthMax(arr, 4))