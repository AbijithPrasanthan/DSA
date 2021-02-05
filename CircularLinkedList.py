class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def InsertEmpty(self,node):
    self.head = node
    self.tail = node
    node.next = self.head
  
  def InsertBeg(self,node):
    if self.head is None:
      self.InsertEmpty(node)
    else:
      node.next = self.head
      self.head = node
      self.tail.next = self.head
    
  def InsertEnd(self,node):
    if self.head.data is None:
      self.InsertEmpty(node)
    else:
      self.tail.next = node
      self.tail = node
      self.tail.next = self.head
  
  def InsertBtw(self,node,pos):
    temp = self.head
    if self.head.data is None:
      self.InsertEmpty(node)
    else:
      for i in range(pos-1):
        self.head = self.head.next
      node.next = self.head.next
      self.head.next = node
      self.head= temp
  
  def deleteEnd(self):
    if self.head is None:
      return
    else:
      if(self.head == self.tail):
        self.head = None
        self.tail = None
      else:
        temp = self.head
        while(temp.next is not self.tail):
          temp = temp.next
        self.tail = temp
        self.tail.next = self.head

  def deletebeg(self):
    if(self.head == None):    
      return;    
    else:        
      if(self.head != self.tail ):    
        self.head = self.head.next;    
        self.tail.next = self.head;   
      else:
        self.head = None
        self.tail = None

  def deleteBtw(self,pos):
    if(pos == 0):
      self.deletebeg()
    else:
      if(self.head == None):
        return 
      else:
        if(self.head == self.tail):
          self.head = None
          self.tail = None
        else:
          temp = self.head
          for _ in range(pos-1):
            temp = temp.next
          temp.next = temp.next.next
  
  def traversal(self):
    temp = self.head
    while(self.head != self.tail):
      print(self.head.data,end='->')
      self.head = self.head.next
    self.head = temp
    print(self.tail.data)

  def search(self,ele):
    temp = self.head
    while(temp is not self.tail):
      if(temp.data == ele):
        print('The searched element ' + str(ele) + ' is present inside the linked list')
        return
      temp = temp.next
    print(str(ele) + ' Not Found')

def main():
  ll = LinkedList()
  ll.InsertBeg(Node(1))
  ll.InsertBeg(Node(2))
  ll.InsertEnd(Node(10))
  ll.InsertEnd(Node(5))
  ll.InsertBeg(Node(7))
  ll.InsertBeg(Node(4))
  ll.InsertBeg(Node(8))
  ll.InsertBeg(Node(9))
  ll.InsertBtw(Node(11),3)
  ll.InsertBtw(Node(12),4)
  ll.InsertEnd(Node(16))
  print('Original Linked List')
  ll.traversal()
  ll.search(7)
  ll.search(20)
  ll.deletebeg()
  ll.deleteEnd()
  ll.deleteBtw(3)
  ll.deleteEnd()
  print('Linked List After Deletion')
  ll.traversal()


if __name__ == "__main__":
  main()
