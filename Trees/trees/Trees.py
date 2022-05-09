class Node:
    """
    This class for structring the node .

    The Node  consists of a 'value' that holds 
    the node's value, and a 'next' that holds the 
    address of the next node

    """
    def __init__(self, value):
        self.value  = value
        self.next = None
        
class Queue:
    """
    Queue is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both its ends.
    One end is always used to insert data (enqueue) and the other is used to remove data (dequeue).
    """
    def __init__(self):
        self.front=None
        self.rear=None
        self.len=0

    def enqueue(self,value):
        """
        This function will always add new nodes in the  Queue.
        The new node is always added before the last"rear" element of the given Queue.
       
        """
        
        if not isinstance(value, Node):
            node = Node(value)
        
        if self.front is None:
            self.front = node
            self.rear=node
            self.len+=1
        else:
            self.rear.next=node 
            self.rear= node
            self.len+=1
            
    def dequeue(self) :  
        """
        This function will always remove the front nodes in the  Queue.
        The removed node is always removed from the head"front" element of the given Queue.
       
        """ 
        temp = self.front        
        
        self.front = self.front.next 
        
        temp.next = None  
        self.len -=1
        return temp.value
   
    def is_empty(self):
        """
        checks weather the stack is empty -- returns true if its empty
        """
        return self.front == None 
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
            if  type(node.value) != int: 
                raise Exception("All values must be integers !")
        
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
    def breadthfirst_traverse(self):
        """
        doing a breadth first traversal of the tree
        input: none
        output: print the values of the nodes of the tree in the breadth first order
        """
        if not self.root:
            raise(Exception("Tree is empty !"))
        
        output = ''
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            front = queue.dequeue()
            output += f'{front.value} '
        
            if front.left:
                queue.enqueue(front.left)

            if front.right:
                queue.enqueue(front.right)
        
        return output
         

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
# class kNode:
#     def __init__(self, value):
#         self.value = value
#         self.children=[] 
# class K_ary_Tree:
#     def __init__(self):
#         self.root = None           
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
           
        if  type(node.value) != int: 
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
    # tree = [int(i) for i in tree.breadthfirst_traverse().strip().split()]
    # new_tree = []
    # for i in tree:
    #     if i % 3 == 0 and i % 5 == 0:
    #         i = 'FizzBuzz'
    #         new_tree.append(i)
    #     elif i % 3 == 0:
    #         i = 'Fizz'
    #         new_tree.append(i)
    #     elif i % 5 == 0:
    #         i = 'Buzz'
    #         new_tree.append(i)
    #     else:
    #         i = str(i)
    #         new_tree.append(i)
    # print(new_tree)      
    # new_binarytree = BinaryTree()
    # [new_binarytree.add(i) for i in new_tree]
    
    # return new_binarytree
         
if __name__ == "__main__":    
    node1 = TNode(1)
    node2 = TNode('2')
    node3 = TNode(30)
    node4 = TNode(200)
    node5 = TNode(50)
    node6 = TNode(3)
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
    print(f'Breadth First : {tree.breadthfirst_traverse()} \n')
    print('Maximum Value : ',tree.find_maximum())
    print(fizz_buzz_tree(tree).breadthfirst_traverse())