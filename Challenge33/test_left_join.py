from hashtable import HashTable
from left_join import left_join
import pytest

def test_left_join_hashmap():
    hash1 = HashTable()
    hash2 = HashTable()

    [hash1.set(item, key) for item, key in zip(["diligent", "fond", "guide", "outfit", "wrath"], ["employed", "enamored", "usher", "garb", "anger"])]
    [hash2.set(item, key) for item, key in zip(["diligent", "fond", "guide", "flow", "wrath"], ["idle", "averse", "follow", "jam", "delight"])]
        
    assert left_join(hash1, hash2) == [['wrath', 'anger', 'delight'], ['outfit', 'garb', 'Null'], ['diligent', 'employed', 'idle'], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse']]

def test_left_join():
    with pytest.raises(Exception):
        left_join(HashTable(), HashTable())
    
def test_left_join_exception():
    with pytest.raises(Exception):
        left_join([],[])   
    