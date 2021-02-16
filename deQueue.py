class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class deQueue:
    def __init__(self,type):
        self.head = None
        self.type = type

    def InsertRear(self,data):
        node = Node(data)
        if self.head is None:   
            self.head = node
        else:
            temp = self.head
            while(self.head.next):
                self.head = self.head.next
            self.head.next = node
            self.head = temp
            
    def InsertFront(self,data):
        node = Node(data)
        if self.head is None:   
            self.head = node
        else:
            node = Node(data)
            temp = self.head
            self.head = node
            node.next = temp

    def deleteFront(self):
        self.head = self.head.next

    def deleteRear(self):
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        temp.next = None

    def peek(self):
        print('The element at the front of the queue is: ' + str(self.head.data))

def main():
    ch = input('Enter the type of the deque(IR->Input restricted/ OR-> Output restricted): ')
    q = deQueue(ch)
    while(1):
        print('''        1. Insert at Front
        2. Insert at Rear
        3. Delete at Front
        4. Delete at Rear
        5. Peek
        6. Exit
        ''')
        ch = int(input('choice >> '))
        if(ch == 1):
            data = int(input('Enter the data: '))
            q.InsertFront(data)
        elif(ch == 2):
            if(q.type == 'IR'):
                print('Operation Not Permitted for this type of queue')
                continue
            data = int(input('Enter the data: '))
            q.InsertRear(data)
        elif(ch == 3):
            q.deleteFront()
        elif(ch == 4):
            if(type == 'OR'):
                print('Operation Not Permitted for this type of queue')
                continue
            q.deleteRear()
        elif(ch == 5):
            q.peek()
        else:
            break

if __name__ == '__main__':
    main()