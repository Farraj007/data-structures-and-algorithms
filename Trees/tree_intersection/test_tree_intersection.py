import pytest
from tree_intersection import tree_intersection,BinaryTree,TNode

def test_tree_intersection(tree1,tree2):
    assert tree_intersection(tree1,tree2) == {'-5', '10', '2', '33'}

def test_tree_intersection2():
    tree1=BinaryTree()
    tree1.root = TNode(10)
    tree2=BinaryTree()
    tree2.root = TNode(10)
    assert tree_intersection(tree1,tree2) == {'10'}

def test_tree_intersection_exception():
    with pytest.raises(Exception):
        tree_intersection(BinaryTree(),BinaryTree())
        
@pytest.fixture
def tree1():
    
    tree1 = BinaryTree()
    tree1.root = TNode(10)
    tree1.root.right = TNode(15)
    tree1.root.left = TNode(2)
    tree1.root.left.left = TNode(-5)
    tree1.root.right.left = TNode(33)
    
    return tree1

@pytest.fixture    
def tree2():

    tree2= BinaryTree()
    tree2.root = TNode(10)
    tree2.root.right = TNode(20)
    tree2.root.left = TNode(2)
    tree2.root.left.left = TNode(-5)
    tree2.root.right.left = TNode(33)

    return tree2
        

