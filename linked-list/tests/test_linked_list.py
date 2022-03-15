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





# ======
# Fixtures
# ======
# // Aspired and adviced from my collegue Mustafa al Hasannat

@pytest.fixture
def the_linked_list():
    ll = LinkedList()
    [ll.Append(Node(i)) for i in ["Yahya","Emad", "Ammar", "Mustafa", "Zaid"]]
    return ll
