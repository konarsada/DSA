s = ["h","e","l","l","o"]
i = 0
j = len(s)-1
while(i < j):
    '''
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    '''
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1
print(s)