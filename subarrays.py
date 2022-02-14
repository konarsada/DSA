# Given an array, generate all the possible subarrays of the given array.

def subarrays(arr, start, end):
    if(end < len(arr)):
        print(arr[start:end+1])
        subarrays(arr, start, end+1)
    else:
        if(start < len(arr)):
            subarrays(arr, start+1, start+1)

subarrays([1, 2, 3], 0, 0)