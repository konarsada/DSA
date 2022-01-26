'''
Problem Statement: Given a value V, if we want to make a change for V Rs
and we have an infinite supply of each of the denominations in Indian currency,
i.e., we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes,
what is the minimum number of coins and/or notes needed to make the change.
'''

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

def minCoins(V):
    global denominations
    
    denominations.sort(reverse=True)
    
    count = 0
    
    for i in range(len(denominations)):
        if(V == 0):
            break
        
        if(denominations[i] > V):
            continue
        
        else:
            while(V - denominations[i] >= 0):
                count += 1
                V -= denominations[i]
    
    return count

print(minCoins(121))