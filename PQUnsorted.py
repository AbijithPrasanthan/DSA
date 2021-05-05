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
        self.pq.append(n)

    def dequeue(self):
        if(self.isEmpty()):
            print("The queue is empty!!")
            return

        else:
            highest = self.pq[0].pri
            pos = 0
            for i in range(1,len(self.pq)):
                if(self.pq[i].pri < highest):
                    highest = self.pq[i].pri
                    pos = i
            item = self.pq.pop(pos)
            print('Item ' + str(item.data) + ' with priority ' + str(item.pri) +  ' is popped from the queue')

    def traversal(self):
        for i in self.pq:
            print(i.data,end = '->')
        print()
    
if __name__ == '__main__':
    pq = PriorityQueue()
    pq.enqueue(1,1)
    pq.enqueue(2,4)
    pq.enqueue(3,2)
    pq.enqueue(4,5)
    pq.enqueue(5,3)

    pq.traversal()

    print()

    pq.dequeue()
    pq.dequeue()

    print()
    print("The queue after deletion")

    pq.traversal()