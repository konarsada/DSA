def checkReach(maze, final, i, j):
    if(i == n-1 and j == m-1):
        print("Final")
        for elem in final:
            print(elem)
        return
    
    if(i+1 < n and maze[i+1][j]):
        final[i+1][j] = 1
        checkReach(maze, final, i+1, j)
        final[i+1][j] = 0
    
    if(j+1 < m and maze[i][j+1]):
        final[i][j+1] = 1
        checkReach(maze, final, i, j+1)
        final[i][j+1] = 0

maze = [[1, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 0, 1]]

n = len(maze)
m = len(maze[0])

outputMat = [[0 for j in range(m)] for i in range(n)]

print("Maze")
for elem in maze:
    print(elem)

if(maze[0][0]):
    outputMat[0][0] = 1
    checkReach(maze, outputMat, 0, 0)