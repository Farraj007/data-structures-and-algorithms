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

def test_LinkedList_zipped(the_linked_list):
    ll2 = LinkedList()
    [ll2.Append(i) for i in ["5","4", "3", "2","1"]]   
    the_linked_list.linkedListZip(the_linked_list,ll2)
    assert str(the_linked_list) == "Yahya -> 5 -> Emad -> 4 -> Ammar -> 3 -> Mustafa -> 2 -> Zaid -> 1 -> NULL"
    

def test_LinkedList_zipped_list_of1(the_linked_list):
    ll2 = LinkedList()
    [ll2.Append(i) for i in ["5"]]   
    the_linked_list.linkedListZip(the_linked_list,ll2)
    assert str(the_linked_list) == "Yahya -> 5 -> Emad -> Ammar -> Mustafa -> Zaid -> NULL"

def test_LinkedList_zipped_list_bigger_than_the_first():
    ll1=LinkedList()
    ll1.Append('Yahya')
    ll2 = LinkedList()
    [ll2.Append(i) for i in ["5",'4','3']]   
    ll1.linkedListZip(ll1,ll2)
    assert str(ll1) == "Yahya -> 5 -> 4 -> 3 -> NULL"    

# ======
# Fixtures
# ======
# // Aspired and adviced from my collegue Mustafa al Hasannat

@pytest.fixture
def the_linked_list():
    ll = LinkedList()
    [ll.Append(Node(i)) for i in ["Yahya","Emad", "Ammar", "Mustafa", "Zaid"]]
    list=["Yahya","Emad", "Ammar", "Mustafa", "Zaid"]

    return ll
            