def powerSet(ipStr, i=0, cur=""):
    if(i == len(ipStr)):
        print(cur, end=", ")
        return
    
    powerSet(ipStr, i+1, cur + ipStr[i])
    powerSet(ipStr, i+1, cur)

powerSet("abc")