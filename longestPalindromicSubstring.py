def isPal(s):
    start = 0
    end = len(s)-1
    
    while(start < end):
        if(s[start] != s[end]):
            return s[0]
        
        start += 1
        end -= 1

    return s

def longestPalindromicSubstc(str1):
    n = len(str1)
    longestCount = str1[0]
    
    for i in range(n):
        for j in range(n-1, i, -1):
            
            if(str1[i] == str1[j]):
                currentLongest = isPal(str1[i:j+1])
                longestCount = currentLongest if len(currentLongest) > len(longestCount) else longestCount
                break

    return longestCount

print(longestPalindromicSubstc("forgeeksskeegfor"))