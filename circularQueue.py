class CQueue:
    def __init__(self,size):
        self.size = size
        self.Q = [None for _ in range(size)]
        self.front = self.rear = -1
        self.NoOfItems = 0

    def isEmpty(self):
        if(self.front == -1):
            return True
        else:
            return False

    def enqueue(self,data):
        if(self.isEmpty()):
            self.front = 0
            self.rear = 0
            self.Q[self.rear] = data
            self.NoOfItems += 1
        
        elif((self.rear + 1) % self.size == self.front):       # Condition for a full circular queue
            print('The Queue is full !!!')
            return
        
        else:
            self.rear = (self.rear+1)%self.size
            self.Q[self.rear] = data
            self.NoOfItems += 1

    def dequeue(self):
        if self.isEmpty():
            print('The Queue is Empty !!')
            return
        elif self.front == self.rear:
            print('The element ' + str(self.Q[self.front]) + ' is popped out of the queue.')
            self.front = -1
            self.rear = -1
            self.NoOfItems = 0
            return
        else:
            print('The element ' + str(self.Q[self.front]) + ' is popped out of the queue.')
            self.front = (self.front+1)%self.size
            self.NoOfItems -= 1
            return
        
    def peek(self):
        print('The element at the front of the queue is: ' + str(self.Q[self.front]))
        return
    
    def getLength(self):
        print('The number of items in the queue are: ' + str(self.NoOfItems))
        return

def main():
    size = int(input('Enter the number of elements in the circular queue: '))
    q = CQueue(size)
    while(1):
        print('''    1. ENQUEUE
    2. DEQUEUE
    3. PEEK
    4. EXIT
        ''')

        print('choice >>')
        ch = int(input())
        if ch == 1:
            data = int(input('Enter the data to be inserted: '))
            q.enqueue(data)
        elif ch == 2:
            q.dequeue()
        elif ch == 3:
            q.peek()
        else:
            break

if __name__ == "__main__":
    main()