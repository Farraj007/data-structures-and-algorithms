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
        

    def Insert(self,value):
        """
        This function will always add new nodes in the beginning of the linked list.
        The new node is always added before the head of the given Linked List. And newly added node becomes the new head of the Linked List.
        """

        if  value is None:
            print('Missing Argument')
        else:    
            node = Node(value) 
        
            node.next = self.head 
            self.head = node
        # self.head = Node(value,next)
    #   if self.head is None:
    #       self.head = value
    #   else:
    #       value.next = self.head
    #       self.head = value

    # def insertAfter(self, prev_node, value):
 
    # # 1. check if the given prev_node exists
    #     if prev_node is None:
    #         print("The given previous node must inLinkedList.")
    #         return
 
    # # 2. Create new node &
    # # 3. Put in the data
    
    # new_node = Node(value)
 
    # # 4. Make next of new Node as next of prev_node
    # new_node.next = prev_node.next
 
    # # 5. make next of prev_node as new_node
    # prev_node.next = new_node


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

if __name__ == "__main__":
    ll = LinkedList()
    

    # ll.Insert(hind)
    [ll.Append(Node(i)) for i in ["Yahya","Emad", "Ammar", "Mustafa","Zaid"]]
    print(ll)
   
