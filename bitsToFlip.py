def countSetBits(n):
    count = 0
    
    while(n):
        count += 1
        n = n & (n-1)
    
    return count

def flippedCount(a, b):
    xored = a ^ b
    
    bitsToFlip = countSetBits(xored)
    
    return bitsToFlip

a = 10
b = 20

count = flippedCount(a, b)

print(count)