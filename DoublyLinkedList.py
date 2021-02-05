class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        temp = self.head
        while(self.head):
            print(self.head.data,end=' ')
            self.head = self.head.next
        self.head = temp
        
    def InsertEnd(self,node):
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = node
        node.prev = temp
    
    def Insertbeg(self,node):
        temp = self.head
        node.next = temp
        temp.prev = node
        self.head = node

    def InsertBtw(self,pos,target):
        if(pos == 0):
            self.Insertbeg(target)

        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        target.next = temp.next
        target.prev = temp
        temp.next.prev = target
        temp.next =target

    def deleteBeg(self):
        self.head = self.head.next

    def deleteEnd(self):
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        temp.next = None
    
    def search(self,ele):
        temp = self.head 
        while(temp):
            if(temp.data == ele):
               print("The searched element " + str(ele) + " is present in the linked list!!")
               return 1
            temp = temp.next
        print("The searched element " + str(ele) + " is not present in the linked list!!")

def main():
    ll = LinkedList()

    ll.head = Node(23)
    n1 = Node(21)
    n2 = Node(15)

    ll.head.next = n1
    n1.next = n2
    n1.prev = ll.head
    n2.prev = n1
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
