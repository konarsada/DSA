def countAll(s):
    myHash = {}
    for letter in s:
        myHash[letter] = 0
        
    for letter in s:
        myHash[letter] += 1
    return myHash

def countDups(s):
    allCount = countAll(s)
    for letter in allCount:
        if(allCount[letter] > 1):
            print(letter, allCount[letter])

countDups("test string")