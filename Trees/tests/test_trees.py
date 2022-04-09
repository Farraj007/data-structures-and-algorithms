from Trees.trees.Trees import BinaryTree 
import pytest


def test_pre_order(theTree):
    assert theTree.pre_order() == ['A', 'B', 'D', 'E', 'C', 'F']
    
def test_in_order(theTree):
    assert theTree.in_order() == ['D', 'B', 'E', 'A', 'F', 'C']
    
def test_post_order(theTree):
    assert theTree.post_order() == ['D', 'E', 'B', 'F', 'C', 'A']
    with pytest.raises(Exception):
        BinaryTree.post_order()

def test_contains_theTree(theTree):
    assert theTree.contains("A") == True
    assert theTree.contains("B") == True
    assert theTree.contains("C") == True
    assert theTree.contains("Z") == False
    assert theTree.contains("Q") == False


@pytest.fixture
def theTree():
    nodeA = BinaryTree("A")
    nodeB = BinaryTree("B")
    nodeC = BinaryTree("C")
    nodeD = BinaryTree("D")
    nodeE = BinaryTree("E")
    nodeF = BinaryTree("F")
    
    nodeA.left_child = nodeB
    nodeA.right_child = nodeC
    nodeB.left_child = nodeD
    nodeB.right_child = nodeE
    nodeC.left_child = nodeF
    
        
    # tree = BinaryTree()
    nodeA.root = nodeA
    
    return nodeA



