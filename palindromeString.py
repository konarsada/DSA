def isPal(s):
    start = 0
    end = len(s)-1
    
    while(start < end):
        if(s[start] != s[end]):
            print("not palindrome")
            return
        
        start += 1
        end -= 1
    
    print("yes palindrome")
    return

isPal("abba")