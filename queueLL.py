class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.REAR = None
        self.FRONT = None

    def isEmpty(self):
        if(self.REAR == self.FRONT == None):
            return True
        else:
            return False

    def enqueue(self,data):
        node = Node(data)
        if(self.isEmpty()):
           self.FRONT = self.REAR =  node
        else:
            self.REAR.next = node
            self.REAR = node
    
    def dequeue(self):
        if(self.isEmpty()):
            print('The queue is empty !!')
        else:
            print('The dequeued item is: ' + str(self.FRONT.data))
            self.FRONT = self.FRONT.next
    
    def peek(self):
        if(self.isEmpty()):
            print('The queue is empty !!')
        else:
            print('The element at the front of the queue is: ' + str(self.FRONT.data))
    
def main():
    q = Queue()
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

