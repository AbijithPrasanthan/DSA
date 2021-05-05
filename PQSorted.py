class Node:
    def __init__(self,data,pri):
        self.data = data
        self.pri = pri

class PriorityQueue:
    def __init__(self):
        self.pq = list()

    def isEmpty(self):
        if(len(self.pq) == 0):
            return True
        return False

    def enqueue(self,data,pri):
        n = Node(data,pri)
        pos = 0
        for i in range(0,len(self.pq)):
            if(self.pq[i].pri > pri):
                break
            else:
                pos += 1
        self.pq.insert(pos,n)

    def dequeue(self):
        if(self.isEmpty()):
            print("The queue is empty!!")
            return

        else:
            item = self.pq.pop(0)
            print('Item ' + str(item.data) + ' with priority ' + str(item.pri) +  ' is popped from the queue') 


    def traversal(self):
        for i in self.pq:
            print(i.data,i.pri,end = '->\n')
        print()
    
if __name__ == '__main__':
    pq = PriorityQueue()
    pq.enqueue(1,1)
    pq.enqueue(2,4)
    pq.enqueue(3,2)
    pq.enqueue(4,5)
    pq.enqueue(5,3)

    pq.traversal()

    pq.dequeue()
    pq.dequeue()

    print()

    pq.traversal()