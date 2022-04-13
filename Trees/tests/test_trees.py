from trees.Trees import BinaryTree , BinaryTreeSearch ,TNode
import pytest

def test_in_order(theTree):
    assert theTree.in_order() == 'D B E G A F C '
    with pytest.raises(Exception):
        BinaryTree.in_order()
        
def test_pre_order(theTree):
    assert theTree.pre_order() == 'A B D E G C F '
    with pytest.raises(Exception):
        BinaryTree.pre_order()

def test_post_order(theTree):
    assert theTree.post_order() == 'D G E B F C A '
    with pytest.raises(Exception):
        BinaryTree.post_order()

def test_contains_theTree(searchTree):
    assert searchTree.contains(4) == True
    assert searchTree.contains(22) == True
    assert searchTree.contains(200) == True
    assert searchTree.contains(11) == False
    assert searchTree.contains(322) == False

def test_maximum_value(searchTree):
    assert searchTree.find_maximum() == 200
    with pytest.raises(Exception):
        BinaryTree.find_maximum()
        
def test_Exceptions():
    tree=BinaryTree()
    with pytest.raises(Exception):
        tree.pre_order()
    with pytest.raises(Exception):
        tree.in_order()
    with pytest.raises(Exception):
        tree.post_order()
    with pytest.raises(Exception):
        tree.find_maximum()
def test_breadthtraverse(theTree):
    assert theTree.breadthfirst_traverse() == 'A B C D E F G '
    with pytest.raises(Exception):
        BinaryTree.breadthfirst_traverse()
    
@pytest.fixture
def theTree():
    node1 = TNode("A")
    node2 = TNode("B")
    node3 = TNode("C")
    node4 = TNode("D")
    node5 = TNode("E")
    node6 = TNode("F")
    node7 = TNode("G")
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node5.right= node7
        
    tree = BinaryTree() 
    tree.root = node1
    return tree

@pytest.fixture
def searchTree():
    
    search = BinaryTreeSearch()
    search.root=TNode(55)
    [search.add(i) for i in [1,32,45,65,200,30,22,4]]
    return search
