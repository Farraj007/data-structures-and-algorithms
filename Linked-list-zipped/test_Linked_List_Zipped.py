from Linked import LinkedList ,Node

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
