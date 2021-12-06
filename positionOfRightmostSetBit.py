# Write a one line function to return position of first 1 from right to left, in binary representation of an Integer

import math

def positionOfRightmostSetBit(n):
    # n & -n sets the least significant set bit and clears all the other bits
    n = n & -n
    
    return math.log2(n) + 1

print(positionOfRightmostSetBit(12))