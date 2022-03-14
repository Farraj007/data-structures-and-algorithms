
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
   
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
  
    def Add_after(self, target_data, new_data):
        
        if not self.head:
            raise Exception("List is empty")
        current = self.head
        while current.next is not None:
            
            if current.value == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def Add_before(self, target_data, new_data):

        if not self.head:
            raise Exception("List is empty")
        current = self.head
        while current.next is not None:
            if current.next.value == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next  
"""
and the tests below for the above functions 

def test_add_after(the_linked_list):
    the_linked_list.Add_after("Yahya","/ LTUC")
    assert str(the_linked_list) == "Yahya -> / LTUC -> Emad -> Ammar -> Mustafa -> Zaid -> NULL"

def test_before_after(the_linked_list):
    the_linked_list.Add_before("Zaid","/ LTUC")
    assert str(the_linked_list) == "Yahya -> Emad -> Ammar -> Mustafa -> / LTUC -> Zaid -> NULL"   

def test_append_on_the_list(the_linked_list):
    the_linked_list.Append(Node("done"))
    assert str(the_linked_list) == "Yahya -> Emad -> Ammar -> Mustafa -> Zaid -> done -> NULL"





# ======
# Fixtures
# ======
# // Aspired and adviced from my collegue Mustafa al Hasannat

@pytest.fixture
def the_linked_list():
    ll = LinkedList()
    [ll.Append(Node(i)) for i in ["Yahya","Emad", "Ammar", "Mustafa", "Zaid"]]
    return ll
"""

