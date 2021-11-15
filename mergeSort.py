def mergeSort(arr, p, r):
    if(p < r):
        q = (p + r) // 2
        mergeSort(arr, p, q)
        mergeSort(arr, q + 1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    arr1 = []
    arr2 = []
    for i in range(n1):
        arr1.append(arr[p + i])
    for j in range(n2):
        arr2.append(arr[q + j + 1])
    print(arr1, arr2)
    i = 0
    j = 0
    k = p
    while((i < n1) and (j < n2)):
        if(arr1[i] <= arr2[j]):
            arr[k] = arr1[i]
            i += 1
        elif(arr1[i] > arr2[j]):
            arr[k] = arr2[j]
            j += 1
        k += 1
    while(i < n1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    while(j < n2):
        arr[k] = arr2[j]
        j += 1
        k += 1

arr = [7, 4, 9, 12, 8]
mergeSort(arr, 0, len(arr) - 1)
print(arr)