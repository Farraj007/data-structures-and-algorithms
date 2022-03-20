# Challenge Summary
 **Linked list**
 Creating :
### Kth from end method 
>arguments: k
-Search for the kth index from the linked list in a back order and rerurn the value of that node.


## Whiteboard Process
![Whiteboard](./ZippedList.jpg)

## Approach & Efficiency
    `class Node:`
    This class for structring the nodes inside the linked list .

    The Node  consists of a 'value' that holds 
    the node's value, and a 'next' that holds the 
    address of the next node

        
    `def LinkedListZip:`
    This function will Take two arguments (list1,lis2) and connect the two lists together in a pattern . zipping them together in a zigzag way . 
    the first form1 to the first from 2 and then 2nd from 1 and on ,on . 

    there is some edge cases explained in the whiteboard and the code itself
    
    

The complexity is O(n)for the worst case scenaario in my code
           

## Solution
[The code](./Linked_List_Zipped.py)