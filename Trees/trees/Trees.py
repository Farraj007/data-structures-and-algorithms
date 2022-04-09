class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
     
    def in_order(self):
        """
        traverse a tree (in-order --> left-root-right)
        Input: None
        output: print values of the nodes of the tree
        """
        
        output = ''
        def _walk(node):
            nonlocal output 

            if node.left:
                _walk(node.left)

            output += f'{node.value} '

            if node.right:
                _walk(node.right)
            
        _walk(self.root) 
        
        return output
    
    def pre_order(self):
        """
        traverse a tree (pre-order --> root-left-right)
        Input: None
        output: print values of the nodes of the tree
        """
        
        output = ''
        def _walk(node):
            nonlocal output 
            output += f'{node.value} '

            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)
                
            
    
        _walk(self.root)
                
        return output    
    
    def post_order(self):
        """
        traverse a tree (post-order --> left-right-root)
        Input: None
        output: print values of the nodes of the tree
        """
        
        output = ''
        def _walk(node):
            nonlocal output 

            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)
                
            output += f'{node.value} '
            
        _walk(self.root)
        
        return output
    
    def addLeft(self, item):
        new = BinaryTree(item)
        self.left_child = new
        return new.root+" has been added"

    def addRight(self, item):
        new = BinaryTree(item)
        self.right_child = new
        return new.root+" has been added"

    def delLeft(self):
        if self.left_child and self.right_child is None :
            raise Exception ("The Tree is Empty")
        temp = self.left_child.value
        self.left_child = None
        return temp+" has been deleted"


    def traverse_bf(self):
        nodes = [self]
        print(self.value, end=" ")

        while nodes:
            p = nodes.pop(0)
            if p.left_child is not None:
                print(p.left_child.value, end=" ")
                nodes.append(p.left_child)
            if p.right_child is not None:
                print(p.right_child.value, end=" ")
                nodes.append(p.right_child)
        print()

    def height(self):
        height_left = 0
        height_right = 0
        if self is None:
            return 0
        else:
            if self.left_child is not None:
                height_left = self.left_child.height()
            if self.right_child is not None:
                height_right = self.right_child.height()
            if height_left > height_right:
                return height_left + 1
            else:
                return height_right+1

    def count_nodes(self):
        
        def _walk(node):
            left_nodes = right_nodes = 0
            if node.left is None and node.right is None:
                return 1

            left_nodes = right_nodes = 0

            if node.left :
                left_nodes = node.left.count_nodes()

            if node.right :
                right_nodes = node.right.count_nodes()

            _walk(self.root)
            return left_nodes + right_nodes + 1

    def count_leaf(self):
        left_leaves = right_leaves = 0
        
        def _walk(node):
            print(node)
            nonlocal left_leaves , right_leaves        
            if node.left is None and node.right is None:
                return 1
            if node.left :
                left_leaves = node.left.count_leaf()

            if node.right :
                right_leaves = node.right.count_leaf()
                
            
            _walk(self.root)
            return left_leaves + right_leaves

        
        
class BinaryTreeSearch(BinaryTree):
    """
    a binary tree where each left node is less than its root, and each 
    right node is greater than its root 
    """
    
    def add(self, value):
        """
        add the value correctly to the tree
        input: value
        output: None
        """
         
        current = self.root
        
        while True:
            if current.left and value < current.value:
                current = current.left
            elif current.right and value > current.value:
                current = current.right                
            else:
                if value < current.value:
                    current.left = TNode(value)
                else:
                    current.right = TNode(value)
                break         
                
        
    def contains(self, value):
        """        
        check if the value is in the tree at least once
        input: value
        output: boolean 
        """
        if type(value) !=str:
            value = str(value)
        
        return True if value in self.in_order() else False
        
if __name__ == "__main__":    
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
    search = BinaryTreeSearch()
    search.root=TNode(55)
    [search.add(i) for i in [1,32,45,65,200,30,22,4]]
    print(f'In Order: {tree.in_order()} \n')
    print(f'Pre Order: {tree.pre_order()} \n')
    print(f'Post Order: {tree.post_order()} \n')
    print(search.contains(4))
    # print("Breadth First : ")
    # tree.traverse_bf()
    # print()

    # print(f"Height of tree = {node1.height()} \n")
    # print(f"Total nodes = {node1.count_nodes()}\n")
    
    print(f"Total leaves = {tree.count_leaf()}\n ")
