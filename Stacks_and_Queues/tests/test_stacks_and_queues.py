from stacks_and_queues.Stacks_and_queues import Stack, Node,Queue
import pytest

def test_Stacking(my_stack):
    my_stack.push(10)
    assert  my_stack.top.value == 10

def test_stacking_multi(my_stack):
    [my_stack.push(i) for i in [11,12]] 
    assert  my_stack.top.value == 12  
def test_pop_off_stack(my_stack):
    my_stack.pop()
    assert  my_stack.top.value == 'Hi'
    
def test_empty(my_stack):
    [my_stack.pop() for i in range(0,4)]
    with pytest.raises(Exception):
        my_stack.peek()
        
def test_peek_next(my_stack):
    assert my_stack.peek() == 'Hi'  

def test_instantiate_stack():
    stack = Stack()
    assert stack.is_empty() == True
def test_Exce(my_stack):
    [my_stack.pop() for i in range(0,4)]
    with pytest.raises(Exception):
        my_stack.peek()
    with pytest.raises(Exception):
        my_stack.pop()  
          
def  test_enqueue_into_a_queue(my_queue):
    my_queue.enqueue(5)
    assert my_queue.rear.value == 5
    
def test_enqueue_multiple_values_into_a_queue(my_queue):
    [my_queue.enqueue(i) for i in [8,7,6]] 
    assert my_queue.rear.value == 6
def test_dequeue_out_of_a_queue_the_expected_value(my_queue):
    my_queue.dequeue()
    assert my_queue.front.value == 2
    
def test_peek_into_a_queue_seeing_the_expected_value(my_queue):
    assert my_queue.peek() == 1
    
def test_empty_a_queue_after_multiple_dequeues(my_queue):
    [my_queue.dequeue() for i in range(0,4)]

def test_instantiate_an_empty_queue():
      q=Queue()
      assert q.is_empty() == True
def test_queue_raises_exception():
    q=Queue() 
    with pytest.raises(Exception):
        q.peek()
    with pytest.raises(Exception):
        q.dequeue () 
    
@pytest.fixture
def my_stack():
    stack = Stack()
    [stack.push(i) for i in ["!","There", "Hi", "Barham,"]]
    
    return stack

@pytest.fixture
def my_queue():
    queue = Queue()
    [queue.enqueue(i) for i in [1,2,3,4]]
    return queue