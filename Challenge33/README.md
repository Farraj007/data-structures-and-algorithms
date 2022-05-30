# Hashmap left join


## Hashmap LEFT JOIN

The Hashmap LEFT JOIN returns an array that contains all the keys and the values from the left has table, with the values for the right hash tables if they have the same key

## Challenge

Write a function called left join, that takes two hashtables as an input, and returns an array that has the keys and values for the left hashmap, and the values from the right hashmap if they have the same key

## Whiteboard

![whitboard](./hashmap-left-join.png)

## Approach & Efficiency

first step loop over left_hashtable and append it to output list and check if the key is in right hashtable the append key/value of left hashtable and value of right hastable if not  return Null insted of value of right hashtable.

Big O:

- time O(n): because of the for loob
- space O(n): because we are using a list to store the values inside it.

## Solution

[Code](./left_join.py)

[Tests](./left_join_tests.py)