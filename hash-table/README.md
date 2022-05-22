# Hashtables
Hashtables are a type of data structures that stores data as key-value pairs. This means every Node or Bucket has both a key, and a value. Hashing can also be defined as a technique that is used to uniquely identify a specific object from a group of similar objects.

## Challenge
Implement a Hashtable Class with the following methods:
- Method should hash the key, and set the key and value pair in the table, handling collisions as needed.
- Should a given key already exist, replace its value from the value argument given to this method.
- Method that returns: Value associated with that key in the table
- Method that returns: Boolean, indicating if the key exists in the table already.
- Method that returns: Collection of keys
- Method that returns: Index in the collection for that key


## Approach & Efficiency
- hash(self, key) --> time: Big O(n), space: Big O(1)

- set(self, key, value) --> time & space: Big O(1)).

- get(self, key) --> time & space: Big O(1).

- contains(self, key) --> time & space: Big O(1).

- keys(self) --> time & space: Big O(1).


## API

HashTable: Class to create an instance of a HashTable data structure.

init(self, size): method to initalize Hash table instance, takes the integer as a parameter to create a hash table based on array size.

hash(self, key): method that takes a key and returns the index of that key in the table.

set(self, key, value): method that takes key and value. This method hash the key, and add the key and value pair to the table, handling collisions as needed.

get(self, key): method that takes in the key and returns its value from the table.

contains(self, key): method that takes in the key and returns a boolean, indicating if the key exists in the table already.

keys(self): a method that returns the collection of keys.