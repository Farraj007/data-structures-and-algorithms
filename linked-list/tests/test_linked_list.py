from linked_list.linked_list import LinkedList ,Node
import pytest

def test_linkedlist_empty():
    assert LinkedList().head == None

def test_inserting_items():
    assert LinkedList.Insert("Barham") == " Barham -> Yahya -> Emad -> Ammar -> Mustafa -> Zaid -> NULL"

@pytest.fixture
def my_linked_list():
    ll = LinkedList()
    [ll.Append(Node(i)) for i in ["Emad", "Ammar", "Mustafa","Zaid","Yahya"]]
    return ll
