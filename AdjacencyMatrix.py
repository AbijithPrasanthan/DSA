class Graph:
    def __init__(self,size):
        self.adjMat = [[0]*(size+1) for i in range(size+1)]
        self.size = size

    def addEdge(self,n1,n2):
        self.adjMat[n1][n2] = 1
        self.adjMat[n2][n1] = 1

    def remEdge(self,n1,n2):
        if self.adjMat[n1][n2] == 0:
            print('No edge from {} to {}'.format(n1,n2))
            return
        self.adjMat[n1][n2] = 0
        self.adjMat[n2][n1] = 0

    def printGraph(self):
        print('   ',end = '')
        for i in range(self.size+1):
            print(i,end = ' ')
        print()
        print()
        for i in range(self.size+1):
            print(i,end = '  ')
            for j in range(self.size+1):
                print(self.adjMat[i][j],end = ' ')
            print()

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(0,1)
    g.addEdge(0,3)
    g.addEdge(1,3)
    g.addEdge(2,3)
    g.addEdge(1,2)
    g.addEdge(1,5)
    g.addEdge(2,5)
    g.addEdge(2,4)
    g.addEdge(3,4)
    g.addEdge(6,4)
    g.addEdge(1,6)

    g.printGraph()
