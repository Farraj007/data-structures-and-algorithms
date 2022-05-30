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
    def items(self):
        """
        keys(self): a method that returns the collection of keys.
        """
        items = []
        for index in self.table :
            if index:
                for dic in index:
                        [items.append(key) for key in dic.items()]
                        
        return items

