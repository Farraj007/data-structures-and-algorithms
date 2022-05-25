class Node:
    """
    This class for structring the node .

    The Node  consists of a 'value' that holds 
    the node's value, and a 'next' that holds the 
    address of the next node

    """
    def __init__(self, value):
        self.value  = value
        self.next = None
               
class Stack:
    """
    Implementation of Stack ADT based on Py's list.
    For the most efficient ordering, we let the end of the list represent the top of the stack and the front
    represent the base.As the stack grows,items are appended to the end of the list and when items are poppe
    d,they are removed from the same end.
    """
    
    def __init__(self, node = None):
        self.top = node   
         
    def __str__(self):    
        return self.to_string()    
    
    def to_string(self):
        """
        Function to simulate how the Stack will Show 
        """
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
        """
        This funcrion will add a value on the top of the stack .. to stac

        """
        
        if not isinstance(value, Node):
            node = Node(value)
             
        node.next = self.top 
        self.top = node  
      
    def pop(self): 
        """
        This function will remove the top node on the stack .. by making the top for the next value and assign the previous top to none 
        """       
        temp = self.top  
        if temp:
            self.top = self.top.next 
        
            temp.next = None  
        
            return temp.value   
        else:
            raise Exception('The stack is empty')
          
    def peek(self):
        """
        This function will return the value of the Next Top Node if availbe if not will return the value of the top it self .
        Error will raises if the stack is empty
        """
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
    
    """
    Queue is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both its ends.
    One end is always used to insert data (enqueue) and the other is used to remove data (dequeue).
    """
    
    def __init__(self):
        self.front=None
        self.rear=None
        self.len=0
        
    def __str__(self):    
        return self.to_string()    
    
    def to_string(self):
        """
        Function to simulate how the Queue will Show 
        """
        output = "|| "
    
        if (self.front and self.rear) is None:
            output = ('Queue is EMPTY!')
        else: 
            current = self.front
            while current:
                output += f'{current.value} '
                current = current.next   
            output += '||'
            return output
        
    def enqueue(self,value):
        
        """
        This function will always add new nodes in the  Queue.
        The new node is always added before the last"rear" element of the given Queue.
       
        """
        
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
         
        """
        This function will always remove the front nodes in the  Queue.
        The removed node is always removed from the head"front" element of the given Queue.
       
        """ 
        temp = self.front        
        
        self.front = self.front.next 
        
        temp.next = None  
        self.len -=1
        return temp.value
    
    def peek(self):
        
        """
        This function will return the value of the Head Node /The front value.
        Error will raises if the queue is empty
        """
        if self.front:
            return self.front.value 
        else:
            raise Exception("The top Value is None")
    
    def is_empty(self):
        """
        checks weather the stack is empty -- returns true if its empty
        """
        return self.front == None 
    
def DuckDuckGoose(list,k):
    queue =  Queue()
    [queue.enqueue(i) for i in list ]
    
    print('1',queue)
    counter=0
    
    while queue.len > 1:
        counter +=1
        if counter != int(k) and not queue.is_empty(): 
            queue.enqueue(queue.dequeue())
            print(queue)
           
        elif counter == int(k) and not queue.is_empty():
            queue.dequeue() 
            counter = 0   
                  
        elif queue.is_empty():
            raise Exception ('The Queue is Empty')
        
    return queue    
     
def validateBrackets(string):
    
        """
        This function will validate the brackets from a string if it's balanced or not .
        and return a boolean of the answer.
        """
        stack = Stack()
        dictionary = {'{': '}', '(': ')', '[': ']'}
        if type(string) != str:
            raise Exception('Bracket Validator works only strings')
        
        for char in string:
            if char in '{[(':
                stack.push(char)
            elif char in '}])':
                if dictionary[stack.pop()] != char:
                    return False
        if stack.is_empty():
            return True
        else:
            return False
        
def getMax(list):
    
    stack = Stack()
    [stack.push(i) for i in list if type(i) == int]
    if not stack.top:
        raise Exception("The stack is empty")
    max=stack.top.value
    temp=stack.top.next

    while temp:
        if temp.value>max:
            max=temp.value
        temp=temp.next
    if max:
        print(max)
        return max
    else:
        raise Exception("The stack has no numeric values") 
    
class Node:
    """
    Docstring
    """
    pass

class BinaryTree:
    """
    Docstring
    """

    def pre_order():
        # root >> left >> right
        pass

    def in_order():
        # left >> root >> right
        pass

    def post_order():
        # left >> right >> root
        pass

class BinarySearchTree(BinaryTree):
    """
    Docstring
    """

    def add():
        pass

    def contains():
        pass
                
if __name__ == '__main__':
    
    # getMax([1,5,50,20,-60,'barham'])
    # print(getMax())
    a=['a','b','c','d','e']
    #DuckDuckGoose(a,3)
    print(DuckDuckGoose(a,6))
    
    # pseudo = psuedoQueue()
    # # [psuedo.enqueue for i in [1,2,3]]
    # pseudo.front = Node(1)
    # pseudo.front.next = Node(2)
    # pseudo.front.next.next = Node(3)
    # pseudo.dequeue() 
    # print(pseudo.peek())
    # exp="{()}"
    # if validateBrackets(exp):
    #     print('TRUE')
    # else:
    #     print('False')    
    
    # # print(stack.is_empty())
    # [stack.push(i) for i in ['!','There','Hi','Barham ,']]
    # print(stack)
    # print('The top is :',stack.peek())
    # print('i popped:',stack.pop())
    # print('is it empty ?',stack.is_empty())
    
    # queue = Queue()
    # [queue.enqueue(i) for i in [1,2,3,4]] 
    # print(queue)
    # print('the front is:',queue.peek())
    # print('i removed:',queue.dequeue())
    
    # print('is it empty?',queue.is_empty())
    