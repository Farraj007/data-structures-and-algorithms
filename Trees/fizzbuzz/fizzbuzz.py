def fizz_buzz_tree(tree):
    """Takes in a tree as a single argument. Changes values throughout the tree based on Fizzbuzz logic, and returns a new tree in the same order and structure.
    """
    if not tree.root:
        raise(Exception("Tree is empty !"))

    newTree = BinaryTree()
    newTree.root = tree.root 
        
    def _walk(node):
        
        if node.left:
            _walk(node.left)

        if node.right:
            _walk(node.right)
           
        if not str(node.value).isdigit(): 
            raise Exception("All values must be integers !")
        
        if node.value%3==0 and node.value%5==0:
            node.value = "FizzBuzz"
        elif node.value%5==0:
            node.value = "Buzz"
        elif node.value%3==0:
            node.value = "Fizz"
        else:
            node.value = str(node.value)

    _walk(newTree.root)
            
    return newTree
if __name__ == '__main__':
    from Trees.trees import BinaryTree,TNode
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(30)
    node4 = TNode(200)
    node5 = TNode(50)
    node6 = TNode(11)
    node7 = TNode(40)
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node5.right= node7
        
    tree = BinaryTree() 
    tree.root = node1
    fizz_buzz_tree(tree).breadthfirst_traverse()