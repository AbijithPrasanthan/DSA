class Node:
    def __init__(self,v1,v2,wt):
        self.s,self.d,self.wt = v1,v2,wt

class Graph:
    def __init__(self,vertices):
        self.adjMat = list()
        self.vertices = vertices
        self.edges = 0

    def find(self,parent,vert):
        if parent[vert] == -1:      # we have the absolute parent of the vertex
            return vert
        return self.find(parent,parent[vert])

    def union(self,parent,rank,src,dest):
        srcPar = self.find(parent,src)
        destPar = self.find(parent,dest)
        if rank[srcPar] < rank[destPar]:
            parent[srcPar] = destPar
        if rank[srcPar] > rank[destPar]:
            parent[destPar] = srcPar
        else:
            parent[srcPar] = destPar
            rank[destPar] += 1

    def addEdge(self,v1,v2,weight):
        self.adjMat.append(Node(v1,v2,weight))
        self.edges += 1

    def sort(self):
        for i in range(self.edges):
            for j in range(i+1,self.edges):
                if(self.adjMat[i].wt > self.adjMat[j].wt):
                    self.adjMat[i],self.adjMat[j] = self.adjMat[j],self.adjMat[i]

    def kruskal(self):
        res = list()
        parent = [-1 for i in range(self.vertices)]
        rank = [0 for i in range(self.vertices)]
        
        i,j = 0,0
        self.sort()
        while(i < (self.vertices-1) and j < self.edges):
            #print(self.adjMat[j].s,self.adjMat[j].d)
            srcP = self.find(parent,self.adjMat[j].s)       # find the parent of the source vertex
            destP = self.find(parent,self.adjMat[j].d)      # find the parent of the destination vertex
            #print(srcP,destP)
            if srcP == destP:
                j += 1
                continue
            self.union(parent,rank,srcP,destP)
            res.append([self.adjMat[j].s,self.adjMat[j].d,self.adjMat[j].wt])
            i += 1
            j += 1
        return res
print(
'''
A->0
B->1
C->2
D->3
S->4
T->5
''')
g = Graph(6)
g.addEdge(0,1,6)
g.addEdge(0,2,3)
g.addEdge(0,4,7)
g.addEdge(1,2,4)
g.addEdge(1,3,2)
g.addEdge(1,5,5)
g.addEdge(2,3,3)
g.addEdge(2,4,8)
g.addEdge(3,5,2)
res = g.kruskal()
print('The minimum spanning tree of the graph is: ')
for i in range(len(res)):
    print(res[i])