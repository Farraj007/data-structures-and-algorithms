from logging import exception


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



    def Append(self, node):
        """
        This function inserts a value (Node instance) at 
        the (end) of the linked list
        """

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node   

    def deleteNode(self, key):
        """
        This function to delete a certain node from the linked list .. using the key argument for things you want to delete
        """
         
        current = self.head
 
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

    def InsertAfter(self, prev_node, new_data):
        """
        This Function will allow you to insert a new node after a node of your choice .
        you shoudl give it to arguments (previous node "using next mutiple times to reach the required"previous node" , 
        new node you want to add after the previous one)
        """
 
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node            

if __name__ == "__main__":
    ll = LinkedList()
    

    
    [ll.Append(Node(i)) for i in ["Yahya","Emad", "Ammar", "Mustafa","Zaid"]]
    ll.Insert('barham')
    [ll.Insert(i) for i in ["IN ASAC", "ALL","We Are"]]
    print(ll.Includes("Mustafa"))
    print(ll.Includes("LTUC"))
    ll.InsertAfter(ll.head.next.next,"/ LTUC")
    ll.deleteNode("Zaid")
    
    print(ll)
   
