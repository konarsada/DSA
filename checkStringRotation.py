def checkRotation(str1, str2):
    
    str1 = [letter for letter in str1]
    str2 = [letter for letter in str2]
    
    n = len(str1)
    
    while(n > 0):
        item = str2.pop(0)
        str2.append(item)
        
        if(str1 == str2):
            return True
        
        n -= 1
    
    return False

str1 = "ABCD"
str2 = "CDBD"

rotationArr = checkRotation(str1, str2)
if(rotationArr):
    print("Yes Rotation")
else:
    print("No Rotation")