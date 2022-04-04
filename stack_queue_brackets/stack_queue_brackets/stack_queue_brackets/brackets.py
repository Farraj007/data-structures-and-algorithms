# from Stacks_and_Queues.stacks_and_queues.Stacks_and_queues import Stack
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
          
    def is_empty(self):
        """
        checks weather the stack is empty -- returns true if its empty
        """
        return self.top == None  
    
def validate_brackets(string):
        stack = Stack()
        brackets = {'{': '}', '(': ')', '[': ']'}
        for char in string:
            if char in '{[(':
                stack.push(char)
            elif char in '}])':
                if brackets[stack.pop()] != char:
                    return False
        if stack.is_empty():
            return True
        else:
            return False
            
if __name__ == '__main__':
        
    exp="{()}"
    if validate_brackets(exp):
        print('TRUE')
    else:
        print('FALSE')  