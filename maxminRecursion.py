def getMinMax(low, high, arr):
    if(low == high):
        arr_min = arr[low]
        arr_max = arr[low]
        return (arr_max, arr_min)
    elif(high == low + 1):
        if(arr[low] > arr[high]):
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)
    else:
        mid = int((low + high) / 2)
        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid + 1, high, arr)
    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

if(__name__ =='__main__'):
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_max, arr_min = getMinMax(0, len(arr) - 1, arr)