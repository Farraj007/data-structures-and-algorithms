class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
       

    def __str__ (self):
        return self.value  

class  LinkedList:
    
    def __init__(self):
        self.head = None
        
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
    
    @staticmethod
    def linkedListZip(List1,List2):
        """
        This method will takes two linked lists as arguments and will connect them in a zpping pattern.
        """
        if not isinstance(List1, LinkedList) or not isinstance(List2, LinkedList):
            raise Exception("Not inserting LinkedLists")
            
        if List1.head is None and List2.head is None:
            return None
            
        List1_curr = List1.head
        List2_curr = List2.head
 
        while List1_curr != None and List2_curr != None:
            List1.Add_after(List1_curr,List2_curr)
            List1_curr=List1_curr.next.next 
            List2_curr=List2_curr.next

            # List1_next = List1_curr.next             
            # List2_next = List2_curr.next
            
            # List2_curr.next = List1_next  
    
            # List1_curr.next = List2_curr
            
 
            # List1_curr = List1_next
            # List2_curr = List2_next
            # List2.head = List2_curr
        if List2_curr is not None:
            List1.Append(List2_curr)  
    
        return List1   

if __name__ == '__main__':
    ll = LinkedList()
    [ll.Append(Node(i)) for i in ["Yahya","Emad", "Ammar", "Mustafa", "Zaid"]]
    
    list=LinkedList()
    [list.Append(Node(i)) for i in ["1","2", "3", "4", "5"]]
    ll.linkedListZip(ll,list)
    print(ll)
    

    
            