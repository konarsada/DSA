def partition(arr, p, r):
    x = arr[r]
    i = p-1
    for j in range(p, r):
        if(arr[j] <= x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def kthSmallest(arr, l, r, k):
    k -= 1
    if(l < r):
        q = partition(arr, l, r)
        if(q == k):
            return q
        elif(q > k):
            kthSmallest(arr, l, q-1, k)
        else:
            kthSmallest(arr, q+1, r, k)

arr = [12, 3, 5, 7, 4, 19, 26]
k = 3

kthSmallest(arr, 0, len(arr)-1, k)

print(arr[k-1])