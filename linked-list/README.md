# **Singly Linked List**

Implementation: Singly Linked Lists
Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.
This code will cover the making of the node it self and connecting them togetehr to make a linked list . functions included :
1-Includes to searh for a vlaue
2-Insert for insertation in the first of the linked list 
3.Append to add a node on the end of the linked list 


## Challenge
[Code](./linked_list/linked_list.py)

## Approach & Efficiency
For this, I wanted to make sure I furthered my skills in testing, so I made it a priority (even though it should always be one according to TDD). The testing made this way easier than not doing them and made me understand the importance of TDD

## API
### .Insert 
  - Adds a new node with that value to the head of the list with an O(1) Time performance.

### .Append
  - Adds a new node with that value to the End of the list with an O(1) Time performance.

### .Includes 
  - Indicates whether that value exists as a Node’s value somewhere within the list.

### .to_string
  - Returns: a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"

### .Add_after
  - Will add a new node after a desired node by choice  .
  
### .Add_before
  - Will add a new node before a desired node by choice  .