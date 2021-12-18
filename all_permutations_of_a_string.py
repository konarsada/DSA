def allPermute(ind, arr):
    def swap(arr, ind, i):
        arr[ind], arr[i] = arr[i], arr[ind]
    
    if(ind == len(arr)):
        print(arr)
        return
    
    for i in range(ind, len(arr)):
        swap(arr, ind, i)
        allPermute(ind + 1, arr)
        swap(arr, ind, i)

allPermute(0, ['a', 'b', 'c'])