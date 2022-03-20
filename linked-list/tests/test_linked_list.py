from linked_list.linked_list import LinkedList ,Node
import pytest

def test_linkedlist_empty():
    assert LinkedList().head == None

def test_the_list(the_linked_list):
    assert str(the_linked_list) =="Yahya -> Emad -> Ammar -> Mustafa -> Zaid -> NULL"

def test_inserting_items(the_linked_list):
    the_linked_list.Insert("Barham")
    assert str(the_linked_list) == "Barham -> Yahya -> Emad -> Ammar -> Mustafa -> Zaid -> NULL"
    
def test_head_node(the_linked_list):
    assert the_linked_list.head.value == Node("Yahya").value


def test_inserting_multiple_nodes(the_linked_list):
    [the_linked_list.Insert(i) for i in ["IN ASAC", "ALL","We Are"]]
    assert str(the_linked_list) == "We Are -> ALL -> IN ASAC -> Yahya -> Emad -> Ammar -> Mustafa -> Zaid -> NULL"


def test_search_for_existing_node(the_linked_list):
    assert the_linked_list.Includes("Ammar") == True


def test_search_for_not_existing_node(the_linked_list):
    assert the_linked_list.Includes("LTUC") == False

def test_add_after(the_linked_list):
    the_linked_list.Add_after("Yahya","/ LTUC")
    assert str(the_linked_list) == "Yahya -> / LTUC -> Emad -> Ammar -> Mustafa -> Zaid -> NULL"

def test_before_after(the_linked_list):
    the_linked_list.Add_before("Zaid","/ LTUC")
    assert str(the_linked_list) == "Yahya -> Emad -> Ammar -> Mustafa -> / LTUC -> Zaid -> NULL"   

def test_append_on_the_list(the_linked_list):
    the_linked_list.Append(Node("done"))
    assert str(the_linked_list) == "Yahya -> Emad -> Ammar -> Mustafa -> Zaid -> done -> NULL"

def test_add_in_between(the_linked_list):
    the_linked_list.Add_after("Ammar","/ LTUC")
    assert str(the_linked_list) == "Yahya -> Emad -> Ammar -> / LTUC -> Mustafa -> Zaid -> NULL"

def test_before_before_the_head(the_linked_list):
    the_linked_list.Add_before("Yahya" ,"LTUC")
    assert str(the_linked_list) == "LTUC -> Yahya -> Emad -> Ammar -> Mustafa -> Zaid -> NULL"   

def test_after_the_last_node(the_linked_list):
    the_linked_list.Add_after("Zaid","done")
    assert str(the_linked_list) == "Yahya -> Emad -> Ammar -> Mustafa -> Zaid -> done -> NULL"    

def test_k_greater(the_linked_list):
    with pytest.raises(Exception):
        the_linked_list.kthFromEnd(6)
def test_k_same_length_of_linkedlist(the_linked_list):
    kth=the_linked_list.kthFromEnd(4)
    assert str(kth) ==  "Yahya"    

def test_k_negative(the_linked_list):
    with pytest.raises(Exception):
        the_linked_list.kthFromEnd(-1)    

def test_k_linkedlist_of1():
    ll_of1 = LinkedList()
    ll_of1.Append("Me")
    kth=ll_of1.kthFromEnd(0)
    assert str(kth)=="Me"
    
def test_k_middle_of_linkedlist(the_linked_list):
    kth=the_linked_list.kthFromEnd(2)
    assert str(kth) ==  "Ammar"
    
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
