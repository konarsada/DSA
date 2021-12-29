# Count pairs with given sum

# O(n^2) time
def sumPairsMethod1(arr, target):
    count = 0
    
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if(arr[i] + arr[j] == target):
                count += 1
    
    return count

# O(n) time
def sumPairsMethod2(arr, target):
    count = 0
    my_hash = {}
    
    for elem in arr:
        if(target - elem in my_hash):
            count += my_hash[target-elem]
        
        if(elem in my_hash):
            my_hash[elem] += 1
        else:
            my_hash[elem] = 1
    
    return count
            

count = sumPairsMethod2([4,5,3,2,6], 5)
print(count)