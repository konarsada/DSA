'''
Given an array which contains all elements occurring k times, but one occurs only once. Find that unique element.
'''

import sys

def findUnique(arr, n, k):
    INT_SIZE = 8 * sys.getsizeof(int)
    count = [0] * INT_SIZE
    
    for i in range(INT_SIZE):
        for j in range(n):
            if(arr[j] & 1<<i != 0):
                count[i] += 1
    
    res = 0
    
    for i in range(INT_SIZE):
        res += (count[i] % k) * (1 << i)
    
    return res

arr = [6, 2, 5, 2, 2, 6, 6]
n = len(arr)
k = 3

res = findUnique(arr, n, k)

print(res)