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
    [the_linked_list.Insert(i) for i in ["All", "IN ASAC","We Are"]]
    assert str(the_linked_list) == "We Are -> IN ASAC -> All -> Yahya -> Emad -> Ammar -> Mustafa -> Zaid -> NULL"


def test_search_for_existing_node(the_linked_list):
    assert the_linked_list.Includes("Ammar") == True


def test_search_for_not_existing_node(the_linked_list):
    assert the_linked_list.Includes("LTUC") == False



# ======
# Fixtures
# ======// Aspired and adviced from my collegue Mustafa al Hasannat

@pytest.fixture
def the_linked_list():
    ll = LinkedList()
    [ll.Append(Node(i)) for i in ["Yahya","Emad", "Ammar", "Mustafa","Zaid"]]
    return ll
