class Node:
    def __init__(self, value):
        self.value  = value
        self.next = None
        
class Queue:

    def __init__(self):
        self.front=None
        self.rear=None
        self.len=0

    def enqueue(self,value):
  
        if not isinstance(value, Node):
            node = Node(value)
        
        if self.front is None:
            self.front = node
            self.rear=node
            self.len+=1
        else:
            self.rear.next=node 
            self.rear= node
            self.len+=1
            
    def dequeue(self) :  
      
        temp = self.front        
        
        self.front = self.front.next 
        
        temp.next = None  
        self.len -=1
        return temp.value
   
    def is_empty(self):
        """
        checks weather the stack is empty -- returns true if its empty
        """
        return self.front == None 
class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def breadthfirst_traverse(self):
        
        if not self.root:
            raise(Exception("Tree is empty !"))
        
        output = ''
        queue = Queue()
        queue.enqueue(self.root)

        while queue:
            front = queue.dequeue()
            output += f'{front.value} '
        
            if front.left:
                queue.enqueue(front.left)

            if front.right:
                queue.enqueue(front.right)
        
        return output
         
