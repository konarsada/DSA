# arr[i][0] = job_id, arr[i][1] = deadline, arr[i][2] = profit

# time- O(n^2)
def maxProfit(arr):
    
    # create array of size = max deadline
    arr.sort(key=lambda x: x[1], reverse=True)
    max_deadline = arr[0][1]
    
    deadline = [False] * max_deadline
    
    # sort array in order of decreasing profit
    arr.sort(key=lambda x: x[2], reverse=True)
    
    for elem in arr:
        profit = elem[2]
        time = elem[1]
        job = elem[0]
        
        for i in range(time-1, -1, -1):
            if(deadline[i] == False):
                deadline[i] = job
                break
    
    return deadline

arr = [['a', 2, 100],['b', 1, 19],['c', 2, 27],['d', 1, 25],['e', 3, 15]]
# arr = [['j1', 5, 200],['j2', 3, 180],['j3', 3, 190],['j4', 2, 300],['j5', 4, 120],['j6',2,100]]

maxProfitJobs = maxProfit(arr)

print(maxProfitJobs)