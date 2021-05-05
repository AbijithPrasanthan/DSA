class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def getMin(self):                               # Get Minimum Function
        temp = self
        while(temp.left is not None):
            temp = temp.left
        return temp

    def insert(self,data):                          # Insert Function
        if not self.data:
            self.data = data
            return 
        
        if self.data == data:
            print("Duplicate data not permitted")
            return
        
        if data < self.data:
            if self.left:
                self.left.insert(data)
                return 
            self.left = Node(data)
            return
        
        if self.right:
            self.right.insert(data)
            return
        self.right = Node(data)

    def search(self,data):                         # search Function
        if self.data == data or self is None:
            return self

        if data < self.data:
            return self.left.search(data)

        return self.right.search(data)

    def traverse(self):                             # Tree traversal function
        if self is not None:
            print(self.data)
        if self.left is not None:
            print("Going Left",end = ' ')
            self.left.traverse()
        if self.right is not None:
            print("Going Right",end = ' ')
            self.right.traverse()

    def deletion(self,data):                    # Delete function
        if self is None:
            return self
        
        if data < self.data:
            self.left = self.left.deletion(data)

        elif data > self.data:
            self.right = self.right.deletion(data)
        
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp

            elif self.right is None:
                temp = self.left
                self = None
                return temp

            minm = self.right.getMin()
            self.data = minm.data
            self.right = self.right.deletion(minm.data)
        return self

class Tree:
    def __init__(self):
        self.root = None

    def addRoot(self,data):
        if self.root is None:
            self.root = Node(data)


if __name__ == "__main__":
    t = Tree()
    t.addRoot(20)
    t.root.insert(1)
    t.root.insert(3)
    t.root.insert(51)
    t.root.insert(2)
    t.root.insert(7)
    t.root.insert(8)
    print()
    print('Traversing the tree!!!')
    
    t.root.traverse()
    
    print()
    print("Deleting nodes.")

    t.root.deletion(7)
    t.root.deletion(8)
    t.root.deletion(51)
    
    print()
    print('Traversing the tree!!!')
    
    t.root.traverse()
    print()
    ele = t.root.search(3)
    print("Searching for element 3 in the tree")
    if ele:
        print("The element was found in the Binary search tree")
    else:
        print("Element not found")