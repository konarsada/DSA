for n in range(int(input())):
    rows, cols = map(int, input().split())
    myTable = [[0 for j in range(cols+2)] for i in range(rows+2)]
    for row in range(1, rows+1):
        colArr = list(input())
        colArrInd = 0
        for col in range(1, cols+1):
            myTable[row][col] = colArr[colArrInd]
            colArrInd += 1
    currentMax = 0
    # Down Border
    for i in range(1, rows+1):
        maxBorder = 0
        for j in range(1, cols+1):
            if(myTable[i][j] == "#" and myTable[i+1][j] != "#"):
                maxBorder += 1
            if(myTable[i][j] == "#" and myTable[i+1][j] == "#"):
                maxBorder = 0
            if(currentMax < maxBorder):
                currentMax = maxBorder
    # Up Border
    for i in range(1, rows+1):
        maxBorder = 0
        for j in range(1, cols+1):
            if(myTable[i][j] == "#" and myTable[i-1][j] != "#"):
                maxBorder += 1
            if(myTable[i][j] == "#" and myTable[i-1][j] == "#"):
                maxBorder = 0
            if(currentMax < maxBorder):
                currentMax = maxBorder
    # Left Border
    for i in range(1, rows+1):
        maxBorder = 0
        for j in range(1, cols+1):
            if(myTable[i][j] == "#" and myTable[i][j-1] != "#"):
                maxBorder += 1
            if(myTable[i][j] == "#" and myTable[i][j-1] == "#"):
                maxBorder = 0
            if(currentMax < maxBorder):
                currentMax = maxBorder
    # Right Border
    for i in range(1, rows+1):
        maxBorder = 0
        for j in range(1, cols+1):
            if(myTable[i][j] == "#" and myTable[i][j+1] != "#"):
                maxBorder += 1
            if(myTable[i][j] == "#" and myTable[i][j+1] == "#"):
                maxBorder = 0
            if(currentMax < maxBorder):
                currentMax = maxBorder
    print(currentMax)