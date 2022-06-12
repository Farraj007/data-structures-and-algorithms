from hashtable import HashTable

def left_join(left_hash, right_hash):
    if not isinstance(left_hash, HashTable) or not isinstance(right_hash, HashTable):
        raise Exception("Arguments must be hashmaps !")
       
if __name__ == '__main__':

    left_hash = HashTable()
    left_hash.set('diligent', 'employed')
    left_hash.set('fond', 'enamored')
    left_hash.set('guide', 'usher')
    left_hash.set('outfit', 'garb')
    left_hash.set('wrath', 'anger')

    right_hash= HashTable()
    right_hash.set('diligent', 'idle')
    right_hash.set('fond', 'averse')
    right_hash.set('guide', 'follow')
    right_hash.set('flow', 'jam')
    right_hash.set('wrath', 'delight')

    print(left_join(left_hash, right_hash))