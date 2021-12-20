def factorial(n):
    arr = [0]
    
    arr[0] = 1
    arr_size = 1
    
    x=2
    while(x <= n):
        carry = 0
        for i in range(arr_size):
            prod = x * arr[i] + carry
            arr[i] = prod % 10
            carry = prod // 10
        x += 1
        
        while(carry):
            arr.append(carry % 10)
            carry = carry // 10
            arr_size += 1
    
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end="")