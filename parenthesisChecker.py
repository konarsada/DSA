def matchParenthesis(str1):
    opening = ['[', '{', '(']
    
    stack = []
    top = -1
    
    for char in str1:
        if char in opening:
            stack.append(char)
            top += 1
        else:
            if(top >= 0):
                item = stack.pop()
                if(item == '{' and char != '}'):
                    return False
                elif(item == '[' and char != ']'):
                    return False
                elif(item == '(' and char != ')'):
                    return False
                top -= 1
            else:
                return False
    
    if(len(stack) > 0):
        return False
    
    return True

print(matchParenthesis("{{}[]}(([[{}]]))"))