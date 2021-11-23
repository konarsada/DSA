'''

Length of longest common subsequence in two different strings

# Recursion

def LCS(X, Y, n, m):
    if(n == 0 or m == 0):
        return 0
    elif(X[n-1] == Y[m-1]):
        return 1 + LCS(X, Y, n-1, m-1)
    else:
        return max(LCS(X, Y, n-1, m), LCS(X, Y, n, m-1))

X = "AGGTAB"
Y = "GXTXAYB"

print(LCS(X, Y, len(X), len(Y)))   

# DP

def lcs(x, y):
    m = len(x)
    n = len(y)
    
    # matrix to store dp values
    mat = [[None for i in range(n+1)] for j in range(m+1)]
    
    # build mat[m+1][n+1] in bottom up
    for i in range(m+1):
        for j in range(n+1):
            if(i == 0 or j == 0):
                mat[i][j] = 0
            elif(x[i-1] == y[j-1]):
                mat[i][j] = 1 + mat[i-1][j-1]
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])
    
    return mat[m][n]

X = "AGGTAB"
Y = "GXTXAYB"

print(lcs(X, Y))

'''

'''
Length of longest repeating subsequence in a string

LCS(str, str)where str is the input string with the
    restriction that when both the characters are same,
    they shouldn't be on the same index in the two strings.
'''

def longestRepeatingSubsequence(str1):
    
    n = len(str1)
    
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if(str1[i-1] == str1[j-1] and i != j):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    return dp[n][n]

print(longestRepeatingSubsequence("aabb"))