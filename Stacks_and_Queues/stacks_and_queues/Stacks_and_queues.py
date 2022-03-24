from black import out


class Node:
    def __init__(self, value):
        self.value  = value
        self.next = None
        
        
class Stack:
    def __init__(self, node = None):
        self.top = node   
         
    def __str__(self):    
        return self.to_string()    
    
    def to_string(self):
        output = ""
    
        if self.top is None:
            output = ('Stack is EMPTY!')
        else: 
            current = self.top
            while current:
                output += f'\n  {current.value}  \n'
                current = current.next
              
        return output

    def push(self, value):
        
        if not isinstance(value, Node):
            node = Node(value)
            
        # node = Node(value)  
        node.next = self.top 
        self.top = node  
        
    def pop(self): 
                
        temp = self.top  
        if temp:
            self.top = self.top.next 
        
            temp.next = None  
        
            return temp.value   
        else:
            raise Exception('The stack is empty')
          
    def peek(self):
        ref= self.top
        if ref is None:
            raise Exception('There is no Top Value')
        elif ref.next:
            return ref.next.value
        else :
            return ref.value 
        
    
    def is_empty(self):
        """
        checks weather the stack is empty -- returns true if its empty
        """
        return self.top == None    
    
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        
    def __str__(self):    
        return self.to_string()    
    
    def to_string(self):
        output = "|| "
    
        if (self.front and self.rear) is None:
            output = ('Queue is EMPTY!')
        else: 
            current = self.front
            while current:
                output += f'{current.value} '
                current = current.next   
            output += '||'
            return output[::-1]
        
    def enqueue(self,value):
        
        if not isinstance(value, Node):
            node = Node(value)
        
        if self.front is None:
            self.front = node
            self.rear=node
        else:
            self.rear.next=node 
            self.rear= node
            
    def dequeue(self) :   
        temp = self.front        
        
        self.front = self.front.next 
        
        temp.next = None  
        
        return temp.value
    
    def peek(self):
        
        if self.front:
            return self.front.value 
        else:
            raise Exception("The top Value is None")
    
    def is_empty(self):
        """
        checks weather the stack is empty -- returns true if its empty
        """
        return self.front == None  
        
if __name__ == '__main__':
    
    # stack = Stack()
    # # print(stack.is_empty())
    # [stack.push(i) for i in ['!','There','Hi','Barham ,']]
    # print(stack)
    # print('The top is :',stack.peek())
    # print('i popped:',stack.pop())
    # print('is it empty ?',stack.is_empty())
    
    queue = Queue()
    [queue.enqueue(i) for i in [1,2,3,4]] 
    print(queue)
    print('the front is:',queue.peek())
    print('i removed:',queue.dequeue())
    
    print('is it empty?',queue.is_empty())
    
    