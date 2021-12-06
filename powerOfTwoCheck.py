# Given a positive integer, write a function to find if it is a power of two or not.

def powerOfTwo(n):
    n = n & (n-1)
    if(n != 0):
        return False
    else:
        return True

print(powerOfTwo(64))