'''
Find the two non-repeating elements in an array of repeating elements
'''

def twoUnique(arr, n):
    res = 0
    for num in arr:
        res = res ^ num
    
    prod = res & -res
    
    arr1 = []
    arr2 = []
    
    for num in arr:
        if(num & prod != 0):
            arr1.append(num)
        else:
            arr2.append(num)
    
    a = 0
    for num in arr1:
        a = a ^ num
    
    b = a ^ res
    
    return (a, b)

arr = [2, 3, 7, 9, 11, 2, 3, 11]

a, b = twoUnique(arr, len(arr))

print(a, b)