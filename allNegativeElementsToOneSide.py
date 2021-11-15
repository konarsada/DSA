def shiftAll(arr):
    low = 0
    high = len(arr) - 1
    while(low < high):
        if(arr[low] < 0 and arr[high] > 0):
            low += 1
            high -= 1
        elif(arr[low] < 0 and arr[high] < 0):
            low += 1
        elif(arr[low] > 0 and arr[high] > 0):
            high -= 1
        else:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1