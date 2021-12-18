def allPaths(i, j, n, m):
    if(i >= n or j >= m):
        return 0
    if(i == n-1 and j == m-1):
        return 1
    return allPaths(i+1, j, n, m) + allPaths(i, j+1, n, m)

print(allPaths(0, 0, 3, 3))