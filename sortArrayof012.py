def sortArr(arr):
    count0 = 0
    count1 = 0
    count2 = 0
    for elem in arr:
        if(elem == 0):
            count0 += 1
        elif(elem == 1):
            count1 += 1
        else:
            count2 += 1
    i = 0
    while(count0):
        arr[i] = 0
        count0 -= 1
        i += 1
    while(count1):
        arr[i] = 1
        count1 -= 1
        i += 1
    while(count2):
        arr[i] = 2
        count2 -= 1
        i += 1

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sortArr(arr)
print(arr)