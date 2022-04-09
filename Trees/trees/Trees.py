class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def addLeft(self, item):
        new = TNode(item)
        self.left_child = new
        return new.root+" has been added"

    def addRight(self, item):
        new = TNode(item)
        self.right_child = new
        return new.root+" has been added"

    def delLeft(self):
        if self.left_child and self.right_child is None :
            raise Exception ("The Tree is Empty")
        
        temp = self.left_child.root
        self.left_child = None
        return temp+" has been deleted"

    def delRight(self):
        if self.left_child and self.right_child is None :
            raise Exception ("The Tree is Empty")
        
        temp = self.right_child.root
        self.right_child = None
        return temp+" has been deleted"

    def in_order(self):
        
        """
        traverse a tree (in-order --> left-root-right)
        Input: None
        output: print values of the nodes of the tree
        """
        if self.left_child and self.right_child is None :
            raise Exception ("The Tree is Empty")
        if self.left_child :
            self.left_child.in_order()

        print(self.root, end=" ")

        if self.right_child:
            self.right_child.in_order()

    def pre_order(self):
        """
        traverse a tree (pre-order --> root-left-right)
        Input: None
        output: print values of the nodes of the tree
        """
        print(self.root, end=" ")
        
        
        if self.left_child:
            self.left_child.pre_order()

        if self.right_child :
            self.right_child.pre_order()

        if self.left_child and self.right_child is None :
            raise Exception ("The Tree is Empty")
        
    def post_order(self):
        """
        traverse a tree (post-order --> left-right-root)
        Input: None
        output: print values of the nodes of the tree
        """
        if self.left_child and self.right_child is None :
            raise Exception ("The Tree is Empty")
        
        if self.left_child :
            self.left_child.post_order()

        if self.right_child :
            self.right_child.post_order()

        print(self.root, end=" ")

    def traverse_bf(self):
        nodes = [self]
        print(self.root, end=" ")

        while nodes:
            p = nodes.pop(0)
            if p.left_child is not None:
                print(p.left_child.root, end=" ")
                nodes.append(p.left_child)
            if p.right_child is not None:
                print(p.right_child.root, end=" ")
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
        if self.left_child is None and self.right_child is None:
            return 1

        left_nodes = right_nodes = 0

        if self.left_child is not None:
            left_nodes = self.left_child.count_nodes()

        if self.right_child is not None:
            right_nodes = self.right_child.count_nodes()

        return left_nodes + right_nodes + 1

    def count_leaf(self):
        if self.left_child is None and self.right_child is None:
            return 1
        left_leaves = right_leaves = 0
        if self.left_child is not None:
            left_leaves = self.left_child.count_leaf()

        if self.right_child is not None:
            right_leaves = self.right_child.count_leaf()

        return left_leaves + right_leaves
class BinaryTreeSearch(BinaryTree):
    """
    a binary tree where each left node is less than its root, and each 
    right node is greater than its root 
    """
    
    def add(self, value):
        """
        input: value
        doing: add the value correctly to the tree
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
        input: value
        doing: check if the value is in the tree at least once
        output: boolean 
        """
        
        return True if value in self.pre_order() else False
if __name__ == "__main__":

    node1 = TNode("A")
    node2 = TNode("B")
    node3 = TNode("C")
    node4 = TNode("D")
    node5 = TNode("E")
    node6 = TNode("F")
    node7 = TNode("G")

    node2.left_child = node3
    node2.right_child = node4

    node5.left_child = node6
    node5.right_child = node7

    node1.left_child = node2
    node1.right_child = node5
    
    tree = BinaryTree() 
    tree.root = node1


    print("In Order : " , end=" ")
    tree.in_order()
    print()

    print("Pre Order : ")
    tree.pre_order()
    print()

    print("Post Order :  ")
    tree.post_order()
    print()

    print("Breadth First : ")
    tree.traverse_bf()
    print()

    print(f"Height of tree = {tree.height()} \n")
    print(f"Total nodes = {tree.count_nodes()}\n")

    print(f"Total leaves = {tree.count_leaf()}\n ")
