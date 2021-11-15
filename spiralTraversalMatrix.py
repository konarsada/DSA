def spiralPrint(m, n, arr):
    r = 0
    c = 0
    
    while(r < m and c < n):
        for i in range(c, n):
            print(arr[r][i], end = " ")
        r += 1
        
        for i in range(r, m):
            print(arr[i][n-1], end = " ")
        n -= 1
        
        if(r < m):
            for i in range(n-1, c-1, -1):
                print(arr[m-1][i], end = " ")
            m -= 1
        
        if(c < n):
            for i in range(m-1, r-1, -1):
                print(arr[i][c], end = " ")
            c += 1

# Driver Code
a = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

R = 3
C = 6

# Function Call
spiralPrint(R, C, a)