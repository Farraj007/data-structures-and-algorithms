class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
       

    def __str__ (self):
        return self.value  

class  LinkedList:
    
    def __init__(self):
        self.head = None

    def kthFromEnd(self, k):
            n = 0
            curr = self.head
        
            while curr:
                curr = curr.next
                n += 1
                      
            if k > 0:
                if n > k:
                    curr = self.head
                
                    for _ in range(n - (k+1)):
                        curr = curr.next 
                else:
                    raise  Exception ('The Index provided is Not Found')
            else:
                raise Exception('Please Provide Positive Integar For The Search')      
                
                    
            return curr
        
# def test_k_greater(the_linked_list):
#     with pytest.raises(Exception):
#         the_linked_list.kthFromEnd(6)
# def test_k_same_length_of_linkedlist(the_linked_list):
#     kth=the_linked_list.kthFromEnd(4)
#     assert str(kth) ==  "Yahya"    

# def test_k_negative(the_linked_list):
#     with pytest.raises(Exception):
#         the_linked_list.kthFromEnd(-1)    

# def test_k_linkedlist_of1():
#     ll_of1 = LinkedList()
#     ll_of1.Append("Me")
#     kth=ll_of1.kthFromEnd(0)
#     assert str(kth)=="Me"
    
# def test_k_middle_of_linkedlist(the_linked_list):
#     kth=the_linked_list.kthFromEnd(2)
#     assert str(kth) ==  "Ammar"

# # ======
# # Fixtures
# # ======
# # // Aspired and adviced from my collegue Mustafa al Hasannat

# @pytest.fixture
# def the_linked_list():
#     ll = LinkedList()
#     [ll.Append(Node(i)) for i in ["Yahya","Emad", "Ammar", "Mustafa", "Zaid"]]
#     list=["Yahya","Emad", "Ammar", "Mustafa", "Zaid"]

#     return ll
# you can run the test it self by going to the main Linked-list folder 
# you will find the same tests there
#