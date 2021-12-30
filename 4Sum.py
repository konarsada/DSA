# Given an array of integers, find all combination of
# four elements in the array whose sum is equal to a given
# value X

# Time- O(n^4)
def find4Numbers_1(arr, n, X):
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range (k+1, n):
                    if(arr[i] + arr[j] + arr[k] + arr[l] == X):
                        print(arr[i], arr[j], arr[k], arr[l])

# Time- O(n^3)
def find4Numbers_2(arr, n, X):
    arr.sort()
    
    for i in range(n-3):
        for j in range(i+1, n-2):
            l = j+1
            r = n-1
            while(l<r):
                if(arr[i] + arr[j] + arr[l] + arr[r] == X):
                    print(arr[i], arr[j], arr[l], arr[r])
                    l += 1
                    r -= 1
                elif(arr[i] + arr[j] + arr[l] + arr[r] < X):
                    l += 1
                else:
                    r -= 1

# Given an array of integers, find anyone combination of
# four elements in the array whose sum is equal to a given
# value X

# Time- O(n^2)
def find4Numbers_3(arr, n, X):
    my_hash = {}
    
    for i in range(n-1):
        for j in range(i+1, n):
            my_hash[arr[i] + arr[j]] = [i, j]
    
    for i in range(n-1):
        for j in range(i+1, n):
            
            sum21 = arr[i] + arr[j]
            
            if(X - sum21 in my_hash):
                sum22 = my_hash[X - sum21]
                if(sum22[0] != i and sum22[0] != j
                       and sum22[1] != i and sum22[1] != j):
                    print(arr[i], arr[j], arr[sum22[0]], arr[sum22[1]])
                    return

arr = [2,3,4,5,7,8,6,9]
n = len(arr)
X = 23

find4Numbers_3(arr, n, X)