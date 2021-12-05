# log(n) time
def numSetBits(n):
    count = 0
    
    while(n):
        if(n & 1 == 1):
            count += 1
        n = n >> 1
    
    return count
        

# Best time = num set bits
def countSetBits(n):
    count = 0
    
    while(n):
        count += 1
        n = n & (n-1)
    
    return count

num = 13

count = numSetBits(num)

print(count)