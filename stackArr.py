def push(data,stack,TOP):
    stack.append(data)
    TOP+=1
    return stack,TOP

def pop(stack,TOP):
    if(isEmpty(stack)):
        print('The stack is empty !!!')
    else:
        print(str(stack[TOP]) + ' is popped out.')
        TOP -= 1
    return stack,TOP

def isEmpty(stack):
    if(len(stack) == 0):
        return True
    else:
        return False

def peek(stack,TOP):
    return stack[TOP]

def main():
    stack = []
    TOP = -1
    while(1):
        print('''
    1. PUSH
    2. POP
    3. PEEK
    4. EXIT
        ''')

        print('choice >>')
        ch = int(input())
        if ch == 1:
            data = int(input('Enter the data to be inserted: '))
            stack,TOP = push(data,stack,TOP)
        elif ch == 2:
            stack,TOP = pop(stack,TOP)
        elif ch == 3:
            print('The topmost element is: ' + str(peek(stack,TOP)))
        else:
            break

if __name__ == "__main__":
    main()