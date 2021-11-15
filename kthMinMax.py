def partition(arr, low, high):
    x = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if(arr[j] <= x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if(len(arr) == 1):
        return arr
    if(low < high):
        q = partition(arr, low, high)
        quicksort(arr, low, q-1)
        quicksort(arr, q+1, high)

arr = [10, 7, 8, 9, 12, 5]
quicksort(arr, 0, len(arr)-1)
print(arr)    