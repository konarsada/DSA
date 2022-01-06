# adjacency matrix for a graph
class Graph:
    # number of vertices
    n = 0
    
    # adj matrix to represent g
    g = []
    
    # initializing graph
    def __init__(self, num_vertices):
        self.n = num_vertices
        
        for row in range(self.n):
            cols = [0] * self.n
            self.g.append(cols)
    
    # display graph
    def displayAdjMat(self):
        for row in self.g:
            print(row)
        print()
    
    # add edge
    def addEdge(self, x, y):
        if(x > self.n or y > self.n):
            print("Vertex does not exist")
        elif(x == y):
            print("Same vertex")
        else:
            self.g[x-1][y-1] = 1
            self.g[y-1][x-1] = 1

g = Graph(5)

g.displayAdjMat()

g.addEdge(1,5)

g.displayAdjMat()