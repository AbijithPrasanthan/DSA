class Node:
    def __init__(self,data,pri):
        self.data = data
        self.pri = pri

class PriQueue:
    def __init__(self,max):
        self.maxSize = max
        self.pq = list()
        self.pq = [0 for i in range(self.maxSize)]
        self.n = 0

    def isEmpty(self):
        if self.n == 0:
            return True
        return False

    def enqueue(self,data,pri):
        self.n += 1
        self.pq[self.n] = Node(data,pri)
        i = self.n
        while(i > 1 and self.pq[i//2].pri > self.pq[i].pri):
            self.pq[i//2],self.pq[i] = self.pq[i],self.pq[i//2]
            i//=2
    
    def makeHeap(self,ind):
        minInd = ind

        l = 2*ind
        r = (2*ind)+1

        if(l <= self.n and self.pq[l].pri < self.pq[minInd].pri): 
            minInd = l
        
        if(r <= self.n and self.pq[r].pri < self.pq[minInd].pri): 
            minInd = r
        
        if ind != minInd:
            self.pq[ind],self.pq[minInd] = self.pq[minInd],self.pq[ind]
            self.makeHeap(minInd)

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty !")

        elif len(self.pq) == 1:
            item = self.pq.pop(n)
            self.n -= 1
            print('Item ' + str(item.data) + ' with priority ' + str(item.pri) +  ' is popped from the queue') 

        else:
            item = self.pq[1]
            self.pq[1] = self.pq[self.n]
            self.n-=1
            self.makeHeap(1)
            print('Item ' + str(item.data) + ' with priority ' + str(item.pri) +  ' is popped from the queue') 


    def printpq(self):
        pqRepr='''
    / \\
   /   \\
  /     \\
 /       \\
        '''
        for i in range(1,self.n+1):
            if(2*i+1 <=self.n):
                print("Root: " + str(self.pq[i].data))
                print(pqRepr)
                print(str(self.pq[2*i].data),end = "         ")
                print(str(self.pq[2*i+1].data))
                print()
            elif(2*i <= self.n):
                print("Root: " + str(self.pq[i].data))
                print(pqRepr)
                print(str(self.pq[2*i].data),end = "         ")
                print(None)
                print()
            else:
                print("Leaf Nodes: " + str(self.pq[i].data))


if __name__ == '__main__':
    pq = PriQueue(50)
    pq.enqueue(1,1)
    pq.enqueue(2,4)
    pq.enqueue(3,2)
    pq.enqueue(4,5)
    pq.enqueue(5,3)

    pq.printpq()

    pq.dequeue()

    pq.printpq()