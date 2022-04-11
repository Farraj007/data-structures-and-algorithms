from curses.ascii import isdigit


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
        if not self.root:
            raise(Exception("Tree is empty !"))
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
        if not self.root:
            raise(Exception("Tree is empty !"))
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
        if not self.root:
            raise(Exception("Tree is empty !"))
        
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
    
    def traverse_bf(self):
        nodes = [self]
        def _walk(node):
            nonlocal nodes

            if node.left :
                nodes.append(node.left)
                print(node.left.value, end=" ")
            if node.right :
                nodes.append(node.right)
                print(node.right, end=" ")
            if len(nodes) > 0:
                _walk(nodes.pop(0))
                
        return nodes        
    def find_maximum(self):
        """
        return the maximum value from the binary tree
        input: none
        output: number 
        """
        
        if not self.root:
            raise(Exception("Tree is empty !"))
        
        if not self.root.left and not self.root.right:
            return self.root.value
        
        maximum = self.root.value        
        def _walk(node):
            nonlocal maximum 
            
            if node.value > maximum:
                maximum = node.value
            
            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)
                
        _walk(self.root)
        return maximum
        # if type(maximum) == int:
        #     return int(maximum)
        # else:
        #     raise Exception("Not a number")
    

        
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
    search = BinaryTreeSearch()
    search.root=TNode(55)
    [search.add(i) for i in [1,32,45,65,200,30,22,4]]
    print(f'In Order: {tree.in_order()} \n')
    print(f'Pre Order: {tree.pre_order()} \n')
    print(f'Post Order: {tree.post_order()} \n')
    # print(f'Breadth First : {tree.breadth_traversal()} \n')
    print('Maximum Value : ',tree.find_maximum())
    # print(search.contains(4))
    # tree.max()
    # print(f"Height of tree = {tree.height()} \n")
    # print(f"Total nodes = {tree.count_nodes()}\n")
    
    # print(f"Total leaves = {tree.count_leaf()}\n ")
