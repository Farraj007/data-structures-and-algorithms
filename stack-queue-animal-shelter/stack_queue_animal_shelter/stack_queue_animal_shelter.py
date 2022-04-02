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
        else:
            self.rear.next=node 
            self.rear= node
            
    def dequeue(self) :  
        """
        This function will always remove the front nodes in the  Queue.
        The removed node is always removed from the head"front" element of the given Queue.
       
        """ 
        temp = self.front        
        
        self.front = self.front.next 
        
        temp.next = None  
        
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
    
class Dog():
    def __init__(self):
        self.animal_type = 'dog'
           
    
    def __str__(self):
        return f'{self.animal_type}'


class Cat():
    def __init__(self):
        self.animal_type = 'cat'
          

    def __str__(self):
        return f'{self.animal_type}'

   

          

class AnimalShelter:
    """
        AnimalShelter which holds only dogs and cats.
        The shelter operates using a first-in, first-out approach.
        
    """


    def __init__(self):
        self.shelter = Queue()
      
    def __str__(self):
        return f"{self.shelter}"
  
    def enqueue(self,animal):
        """
        enqueue method takes in one argument that inserts an animal object into the queue 
        """
        if not isinstance(animal,Dog) and not isinstance(animal,Cat):
            raise Exception ('animal must be either a Cat or a Dog object')
        else:
            self.shelter.enqueue(animal)




    def dequeue(self,pref=''):
        """
        dequeue method takes in one optional argument that retrieves  the animal the user inputs if it exists.
        if it doesnt it will return the longest stayed animal
        """
        if self.shelter.is_empty():
                raise Exception ('Animal Shelter is empty') 
            
        if pref.lower() == 'dog':
            pref=Dog()     
        elif pref.lower() == 'cat':
            pref = Cat() 
                 
        if str(pref) not in ["cat", "dog"]:
            
            if not self.shelter.is_empty():
                
                return self.shelter.dequeue()
            else:
                raise Exception ('Animal Shelter is empty')
            
        if str(self.shelter.peek()) == str(pref):
            return self.shelter.dequeue()
        
        prev = None
        current = self.shelter.front
        
        while current:
            
            if str(current.value) == str(pref):
                prev.next = current.next
                current.next = None   
                return current.value
            prev = current
            current = current.next
            
    def peek(self):
        return self.shelter.peek()            
        
if __name__ == '__main__':


    animal = AnimalShelter()
    [animal.enqueue(i) for i in [Dog(),Cat(),Cat(),Dog(),Cat(),Dog()]]
    # animal.dequeue()
    print(animal)
    # animal.dequeue()
    animal.dequeue('lizard')
    # animal.dequeue('cat')
    print(animal.peek())
    