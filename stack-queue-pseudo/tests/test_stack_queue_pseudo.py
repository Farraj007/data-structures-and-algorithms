from stack_queue_pseudo.stack_queue_pseudo import psuedoQueue
import pytest

def test_enqueue():
    q = psuedoQueue()
    q.enqueue('Me')
    assert q.dequeue() == "Me"

def test_dequeue(my_pseudo_queue):
    assert my_pseudo_queue.dequeue() == "Hi"

def test_dequeue_empty():
    with pytest.raises(Exception):
        psuedoQueue().dequeue()




@pytest.fixture
def my_pseudo_queue():
    q = psuedoQueue()
    [q.enqueue(i) for i in ["Hi", "There", "!"]]
    return q
