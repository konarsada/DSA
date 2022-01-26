'''
Given an array of non-negative integers. Our task is to find minimum number of elements
such that their sum should be greater than the sum of rest of the elements of the array.
'''

def minElements(arr):
    arr.sort(reverse=True)
    
    total = 0
    for elem in arr:
        total += elem
    
    total /= 2
    
    count = 0
    while(total > 0):
        total -= arr[count]
        count += 1
    
    return count

arr = [2, 1, 2]
print(minElements(arr))