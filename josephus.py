def josephus(n, k):
    if(n == 1):
        return 0
    else:
        return (josephus(n-1, k) + k) % n

print(josephus(5,3))