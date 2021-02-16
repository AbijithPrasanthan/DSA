class Queue:
    def __init__(self):
        self.queue = list()
        self.REAR = -1
        self.FRONT = -1

    def enqueue(self,data):
        if(self.isEmpty()):
            self.FRONT+=1
            self.REAR += 1
            self.queue.append(data)
        else:
            self.queue.append(data)
            self.REAR += 1
    
    def dequeue(self):
        if(self.isEmpty()):
            print('The Queue is Empty')
        
        else:
            print('The element ' + str(self.queue[self.FRONT]) + ' is popped out of the queue!!')
            self.FRONT+=1
    
    def peek(self):
        if(self.isEmpty()):
            print('The queue is empty')
        else:
            print('The element at the front of the queue is: ' + str(self.queue[self.FRONT]))

    def isEmpty(self):
        if(self.FRONT == self.REAR == -1):
            return True
        else:
            return False

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

