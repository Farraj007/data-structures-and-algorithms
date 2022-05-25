class HashTable(object):
    """
    HashTable: Class to create an instance of a HashTable data structure.

    """
    def __init__(self,size = 1024):
        self.size = size
        self.table = [None] * size

    def hash(self,key):
        """
        hash(self, key): method that takes a key and returns the index of that key in the table.

        """
        if type(key) != str:
            raise Exception("Key must be a string")
        
        sum_ascii_value = 0
        for char in key:
            char_value =  ord(char)
            sum_ascii_value += char_value
        sum_ascii_value = (sum_ascii_value*19) % self.size
        return sum_ascii_value

    def set(self,key,value):
        """
        set(self, key, value): method that takes key and value. This method hash the key, and add the key and value pair to the table, handling collisions as needed.

        """
        if type(key) != str and type(value) != str:
                raise Exception("Key and Value must be strings")
            
        index = self.hash(key)
        
        

        if self.table[index]:
            if key in self.keys():
                for dic in self.table[index]:
                    if key in dic.keys():
                        dic[key] = value
            else:
                self.table[index].append({f"{key}":f"{value}"})
        else:
            self.table[index] = [{f"{key}":f"{value}"}]        
                            
    def get(self,key):
        """
        get(self, key): method that takes in the key and returns its value from the table.

        """
        if type(key) is not str:
            raise Exception("Key must be a string")
        
        index = self.hash(key)
        
        if not self.table[index]:
            return None
        
        for dic in self.table[index]:
            if key in dic.keys():
                return dic[key]
   
    def contains(self,key):
        """
        contains(self, key): method that takes in the key and returns a boolean, indicating if the key exists in the table already.
        """
        if type(key) != str:
            raise Exception("Key must be a string")
        
        index = self.hash(key)
        
        if not self.table[index]:
            return False
        
        for dic in self.table[index]:
            if key in dic.keys():
                return True
            return False
     
    def keys(self):
        """
        keys(self): a method that returns the collection of keys.
        """
        keys = []
        for index in self.table :
            if index:
                for dic in index:
                        [keys.append(key) for key in dic.keys()]
                        
        return keys


def tree_intersection(tree1,tree2):
    """
    tree_intersection(tree1,tree2): method that takes in two trees and returns a list of all the values that are common between the two trees.
    """
   
    if tree1.root is None or tree2.root is None:
        raise Exception('Tree is empty')
     
    hash= HashTable()
    
    def tree_traversal(root1,root2):
        
        if root1.value == root2.value:
            hash.set(str(root1.value), True)
              
        if root1.right and root2.right:
            tree_traversal(root1.right,root2.right)
             
        if root1.left and root2.left:
            tree_traversal(root1.left,root2.left)
            
            
    tree_traversal(tree1.root,tree2.root)
    
    return set(hash.keys())

class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

if __name__ == '__main__':
    tree1 = BinaryTree()
    node1= TNode(150)
    tree1.root = node1
    node1.left= TNode(100)
    node1.right= TNode(250)
    node1.right.left= TNode(200)
    node1.right.right= TNode(350)
    node1.left.right= TNode(160)
    node1.left.left= TNode(75)
    node1.right.right.right= TNode(500)
    node1.right.right.left= TNode(300)
    node1.left.right.right= TNode(175)
    node1.left.right.left= TNode(125)

    tree2 = BinaryTree()
    node2= TNode(42)
    tree2.root= node2	
    node2.left= TNode(100)
    node2.right= TNode(600)
    node2.right.left= TNode(200)
    node2.right.right= TNode(350)
    node2.left.right= TNode(160)
    node2.left.left= TNode(15)
    node2.right.right.right= TNode(500)
    node2.right.right.left= TNode(4)
    node2.left.right.right= TNode(175)
    node2.left.right.left= TNode(125)

    tree1 = BinaryTree()
    tree1.root = TNode(10)
    tree1.root.right = TNode(15)
    tree1.root.left = TNode(2)
    tree1.root.left.left = TNode(-5)
    tree1.root.right.left = TNode(33)


    tree2= BinaryTree()
    tree2.root = TNode(10)
    tree2.root.right = TNode(20)
    tree2.root.left = TNode(2)
    tree2.root.left.left = TNode(-5)
    tree2.root.right.left = TNode(33)

    print(tree_intersection(tree1,tree2))