class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class Graph:
    def __init__(self,size):
        self.adjList = [None for _ in range(size+1)]
        self.size = size

    def addVertex(self,v1,v2):
        
        newnode = Node(v2)
        newnode.next = self.adjList[v1]
        self.adjList[v1] = newnode

        newnode = Node(v1)
        newnode.next = self.adjList[v2]
        self.adjList[v2] = newnode
    
    def print(self):
        for i in range(self.size+1):
            print(i,end = '  ')
            temp = self.adjList[i]
            while(temp):
                print(temp.val,end = ' ')
                temp = temp.next
            print()

    def deleteVertex(self,v1,v2):
        temp = self.adjList[v1]
        while temp:
            if temp.val == v2:
                if temp.next:
                    temp = temp.next
                else:
                    temp = None
                break
            temp = temp.next

        temp = self.adjList[v2]
        while temp:
            if temp.val == v1:
                if temp.next:
                    temp = temp.next
                else:
                    temp = None
                break
            temp = temp.next

if __name__ == '__main__':
    n0,n1,n2,n3,n4,n5,n6 = Node(0),Node(1),Node(2),Node(3),Node(4),Node(5),Node(6)
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

    print('Adjacency list of the Graph is: ')
    print()
    g.print()