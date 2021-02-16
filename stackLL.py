class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.TOP = None
        
    
    def push(self,data):
        temp = self.TOP
        self.TOP = Node(data)
        self.TOP.next = temp
    
    def pop(self):
        if self.IsEmpty():
            print('The Stack Is Empty')
        else:
            print(str(self.TOP.data) + ' is popped out !!')
            self.TOP = self.TOP.next
    
    def IsEmpty(self):
        if self.TOP is None:
            return True
        else:
            return False

    def peek(self):
        if self.IsEmpty():
            print('The stack is empty!!')
        else:
            print('The topmost element on the stack is: ' + str(self.TOP.data))
    
def main():
    stack = Stack()
    while(1):
        print('''    1. PUSH
    2. POP
    3. PEEK
    4. EXIT
        ''')

        print('choice >>')
        ch = int(input())
        if ch == 1:
            data = int(input('Enter the data to be inserted: '))
            stack.push(data)
        elif ch == 2:
            stack.pop()
        elif ch == 3:
            str(stack.peek())
        else:
            break

if __name__ == "__main__":
    main()



            
