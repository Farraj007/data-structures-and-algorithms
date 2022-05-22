# Trees

: Tree is a hierarchical data structure. Main uses of trees include maintaining hierarchical data, providing moderate access and insert/delete operations. Binary trees are special cases of tree where every node has at most two children. 

## Challenge
- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
- Create a Binary Tree class
Define a method for each of the depth first traversals:
- **pre_order**
- **in_order**
- **post_order** which returns an array of the values, ordered appropriately.

- Create a Binary Search Tree class this class should be a sub-class of the Binary Tree Class with the following additional methods:
- **Add**:Adds a new node with that value in the correct location in the binary search tree
- **Contains** :boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
- Add -- Big O(log(n)) time and O(1) space using a while loop
- Contains-- Big O(log(n)) time and O(1) space by calling on of the order methods and search in the return if value is found or not 
- pre order, in_order ,post_order -- Big O(n) time and O(n) space using recursion
- Maximum_value -- Big O(n) time and O(1) .

## API

TNode:
```
    
    class that has properties for the value stored in the node,
    the left child node, and the right child node.
```    
   
BinaryTree:
```     
    Parent class for binary trees which has 3 methods to order the data 
    Pre-order: root >> left >> right
    In-order: left >> root >> right
    Post-order: left >> right >> root
    Input: None
    doing: traverse a tree
    output: returns an array of the values, ordered appropriately.
```    

BinarySearchTree:
```
    A subclass of BinaryTree used to add values to the tree and search for them
Add:
    Arguments: value
    Return: nothing
    Adds a new node with that value in the correct location in the binary search tree.
contains:     
    Argument: value
    Returns: boolean indicating whether or not the value is in the tree at least once.
    
```

- [x] Create Node class
- [x] Create BinaryTree class.
- [x] Create BinarySearchTree class.
- [x] pre_order method
- [x] in_order method
- [x] post_order method
---
- [x] Add method
- [x] Contains method
 