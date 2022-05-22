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

def DuckDuckGoose(str , k ):
        str_queue = Queue()
        
        for char in str: 
            str_queue.enqueue(char)
        print(f'{str_queue}')
        itr = str_queue.front 
        if k == 1 :
            while itr.xt:
                str_queue.dequeue()
                itr = itr.next
            return itr.value

        count = 1
        itr = str_queue.front
        while itr and count < k + 1:
            if count == k and itr.next== None : 
                itr = str_queue.front
                itr.next.next=None   
                print(f'{str_queue} end')  
                str_queue.dequeue() 
                print(f'{str_queue} end')   
                break
            if count == k  and itr.next!= None:
                
                valuee = itr.next.value
                itr.next = itr.next.next
                itr.value = valuee
                count = 1
                continue
            if itr.next == None:
                itr = str_queue.front
                count +=1
                continue
            itr = itr.next
            count+=1
            
            print(f'{str_queue} end')
        return
    
if __name__ == '__main__':
    DuckDuckGoose('ABCDE',)