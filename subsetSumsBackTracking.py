def allSubset(arr, i, cur):
    global flag
    
    if(i == len(arr)):
        if(cur == sum(arr)/2 and flag == 0):
            flag = 1
            print(cur)
        return
    
    allSubset(arr, i+1, cur)
    allSubset(arr, i+1, cur + arr[i])

flag = 0
allSubset([3, 5, 2], 0, 0)