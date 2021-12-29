# Subsets having sum between A and B

# Print subset if sum between A and B
def printSubset(arr):
    global A, B, numSubsets
    
    total = 0
    for elem in arr:
        total += elem
    
    if(total >= A and total <= B):
        numSubsets += 1
        print(arr)

# Find all subsets
def subsetSum(arr, k, cur):    
    if(k == len(arr)):
        printSubset(cur)
        return
    subsetSum(arr, k + 1, cur)
    subsetSum(arr, k + 1, cur + [arr[k]])

A = -1
B = 2
numSubsets = 0

subsetSum([1, -2, 3], 0, [])

print(numSubsets)