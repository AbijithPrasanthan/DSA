class Graph:
    def __init__(self,size):
        self.adjMat = [[] for i in range(size+1)]
        self.size = size

    def addVertex(self,v1,v2):
        self.adjMat[v1].append(v2)

    def BFS(self,start):
        visitedNodes = [None for i in range(self.size+1)]
        queue = list()

        queue.append(start)
        while(len(queue) != 0):
            s = queue.pop(0)
            if not visitedNodes[s]:
                print(s,end=' ')
                visitedNodes[s] = 1
            
            for i in self.adjMat[s]:
                if not visitedNodes[i]:
                    queue.append(i)

    def DFS(self,start):
        visitedNodes = [None for i in range(self.size+1)]
        stack = list()

        stack.append(start)
        while(len(stack) != 0):
            s = stack.pop()
            if not visitedNodes[s]:
                print(s,end=' ')
                visitedNodes[s] = 1
            
            for i in self.adjMat[s]:
                if not visitedNodes[i]:
                    stack.append(i)

if __name__ == '__main__':
    g = Graph(6)
    g.addVertex(0,1)
    g.addVertex(0,3)

    g.addVertex(1,2)
    g.addVertex(1,3)
    g.addVertex(1,5)
    g.addVertex(1,6)

    g.addVertex(2,4)
    g.addVertex(2,5)
    g.addVertex(2,3)

    g.addVertex(3,4)

    g.addVertex(4,6)

    print('DFS for the given graph: ')
    g.DFS(0)
    print('\n\nBFS for the given graph: ')
    g.BFS(0)