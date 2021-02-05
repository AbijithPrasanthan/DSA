class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next

    def InsertEnd(self,node):
        temp = self.head
        while(self.head.next):
            self.head = self.head.next
        self.head.next = node
        self.head = temp
    
    def Insertbeg(self,node):
        temp = self.head
        self.head = node
        node.next = temp

    def InsertBtw(self,pos,target):
        count = 0
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        target.next = temp.next
        temp.next = target

    def deleteBeg(self):
        self.head = self.head.next

    def deleteEnd(self):
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        temp.next = None
    
    def search(self,ele):
        temp = self.head
        while(self.head):
            if(self.head.data == ele):
                print('The element is in the Linked List')
                return 0
            self.head = self.head.next
        print('Element Not Found')
def main():
    ll = LinkedList()
    ll.Insertbeg(Node(1))
    ll.InsertEnd(Node(10))
    ll.InsertEnd(Node(80))
    ll.Insertbeg(Node(50))
    ll.InsertBtw(1,Node(20))
    ll.InsertBtw(3,Node(30))
    ll.traversal()
    ll.deleteBeg()
    ll.deleteEnd()
    print()
    print('Element in the Linked List after deletion: ')
    ll.traversal()
    print()
    ll.search(20)
    ll.search(100)


main()
