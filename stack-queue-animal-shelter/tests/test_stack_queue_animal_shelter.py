from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter,Dog,Cat,Queue
import pytest

def test_enqueue():
    sheltert = AnimalShelter()
    sheltert.enqueue(Cat())
    assert str(sheltert.peek()) == "cat"

def test_enqueue_error(shelter):
    with pytest.raises(Exception): 
        shelter.enqueue(Bird())

def test_dequeue(shelter):
    assert str(shelter.dequeue()) == "dog"

def test_dequeue_2(shelter):
    assert str(shelter.dequeue("dog")) == "dog"
    assert str(shelter.dequeue()) == "cat"
    
def test_Dequeue_unfound_type(shelter):
    assert str(shelter.dequeue("Wolf")) == 'dog'

def test_dequeue_error():
    with pytest.raises(Exception): 
        AnimalShelter().dequeue()
        



@pytest.fixture
def shelter():
    shelter1 = AnimalShelter()
    [shelter1.enqueue(i) for i in [Dog(), Cat(), Cat(), Dog(), Cat(), Dog()]]
    return shelter1
    
