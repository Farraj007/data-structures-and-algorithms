from ast import Pass


class Node:
    """
    This class for structring the nodes inside the linked list .

    The Node  consists of a 'value' that holds 
    the node's value, and a 'next' that holds the 
    address of the next node

    """
    def __init__(self,value):
        self.value = value
        self.next = None
       

    def __str__ (self):
        return self.value  

class  LinkedList:
    
    def __init__(self):
        self.head = None

    def __str__(self):    
        return self.to_string()
        

    def Insert(self,value= None):
        """
        This function will always add new nodes in the beginning of the linked list.
        The new node is always added before the head of the given Linked List. And newly added node becomes the new head of the Linked List.
        """

        if value is None:
            raise Exception('Missing Argument')
           
        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
        else:
          value.next = self.head
          self.head = value

    
    def to_string(self):
        """
        This method converts the object of The linked list to a string in the shape of 
        {a} -> {b} -> {c} -> NULL
        """ 
        output = ""
        

        if self.head is None:
            output = ('Linked List is EMPTY!')
        else: 
            current = self.head
            while current:
                output += f'{current.value} -> '
                current = current.next
            output += "NULL"  
        return output

    def Includes(self, value):
        """
        This function checks if the provided value is 
        in the linked list or not and return a Boolean
        """
        
        if self.head is None:
            return False
        else:
            current = self.head
            while current.value is not None:
                if value == current.value:
                    return True
                current = current.next
                if current is None:
                    return False
            return False

    def deleteNode(self, key):
        """
        This function to delete a certain node from the linked list .. using the key argument for things you want to delete
        """
         
        current = self.head
        if not isinstance(key, Node):
            key = Node(key)

        if (current is not None):
            if (current.value == key):
                self.head = current.next
                current = None
                return
 
        while(current is not None):
            if current.value == key:
                break
            prev = current
            current = current.next
 
        if(current == None):
            return

        prev.next = current.next
 
        current = None      

    def Append(self, node):
        """
        This function inserts a value (Node instance) at 
        the (end) of the linked list
        """
        if not isinstance(node, Node):
            node = Node(node)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
  
    def Add_after(self, target_data, new_data):
        """
        This Function will allow you to insert a new node after a node of your choice .
        you should give it to arguments (previous node "using next mutiple times to reach the required"previous node" , 
        new node you want to add after the previous one)
        """
        if not isinstance(target_data, Node):
            target_data = Node(target_data)

        if not self.head:
            raise Exception("List is empty")
        current = self.head
        
        while current.next is not None:
           
            if current.value == target_data.value:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        else:
            new_node = Node(new_data)
            new_node.next = current.next
            current.next = new_node
            return
        
    def Add_before(self, target_data, new_data):
        """
        This Function will allow you to insert a new node before a node of your choice .
        you should give it to arguments (the node where you want to add the value before, the value you want to add it )
        """
        if not isinstance(target_data, Node):
            target_data = Node(target_data)

        if not self.head:
            raise Exception("List is empty")
        current = self.head
        
        if current.value == target_data.value:
            
            new_node = Node(new_data)
            new_node.next = self.head
            self.head=new_node
            return 0  
         
        while current.next is not None:
            if current.next.value == target_data.value:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next  
                          
    def kthFromEnd(self, k):
        len = 0
        curr = self.head
    
        while curr:
            curr = curr.next
            len += 1
            
        if k >= 0:
            if len > k:
                curr = self.head
            
                for _ in range(len - (k+1)):
                    curr = curr.next 
            else:
                raise  Exception ('The Index provided is Not Found')
        else:
            raise Exception('Please Provide Positive Integar For The Search')      
            
                
        return curr
    
    @staticmethod
    def linkedListZip(List1,List2):
        
        if not isinstance(List1, LinkedList) or not isinstance(List2, LinkedList):
            raise Exception("Not inserting LinkedLists")
            
        if List1.head is None and List2.head is None:
            return None
            
        List1_curr = List1.head
        List2_curr = List2.head
 
        while List1_curr != None and List2_curr != None:

            List1_next = List1_curr.next             
            List2_next = List2_curr.next
            
            List2_curr.next = List1_next  
            List1_curr.next = List2_curr
            
            
            List1_curr = List1_next
            List2_curr = List2_next
            List2.head = List2_curr
        if List2_curr is not None:
            List1.Append(List2_curr)  
    
        return List1
        
        
              
        
            
                 
            
                
if __name__ == "__main__":
    ll = LinkedList()
    
    [ll.Append(i) for i in ["Yahya","Emad", "Ammar", "Mustafa","Zaid"]]
    # ll.Insert('barham')
    # [ll.Insert(i) for i in ["IN ASAC", "ALL","We Are"]]
    # print(ll.Includes("Mustafa"))
    # print(ll.Includes("LTUC"))
    # ll.deleteNode("Zaid")
    # ll.Add_before("Yahya" ,"LTUC")
    # ll.Add_after("Zaid","/ LTUC")
    # print(ll.kthFromEnd(0))
    
    ll2 = LinkedList()
    
    [ll2.Append(i) for i in ["5","4", "3", "2","1"]]
    # # print(ll)
    # ll.linkedListZip(ll,ll2)
    # print(ll)
    # ll1=LinkedList()
    # ll1.Append('Yahya')
    # ll1.Append('ME')
    # ll1.Append(':::::')
    # ll2 = LinkedList()
    # [ll2.Append(i) for i in ["5",'4']]  
    ll.linkedListZip(ll,ll2)
    print(ll)
