def arrCopy(mat):
    myList = []
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            myList.append(mat[i][j])
    
    return myList

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

m = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]

mat_to_arr = arrCopy(m)

quicksort(mat_to_arr, 0, len(mat_to_arr)-1)

mid = len(mat_to_arr) // 2

median = mat_to_arr[mid]