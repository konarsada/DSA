arr= [-2, -3, 4, -1, -2, 1, 5, -3]

curMax = arr[0]
curSum = 0

for i in range(len(arr)):
    curSum = curSum + arr[i]
    
    if(curSum > curMax):
        curMax = curSum
    
    if(curSum < 0):
        curSum = 0

print(curMax)