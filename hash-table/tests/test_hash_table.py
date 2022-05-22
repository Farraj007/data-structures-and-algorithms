from hash_table.hashtable import HashTable
import pytest


def test_hash_table(hash_table):
    
    assert hash_table.get("name") == 'python'
def test_hash_table_2(hash_table):
    
    assert hash_table.get("AMAZON") == 'AWS'
    
def test_hash_table_3(hash_table):
    assert hash_table.contains("name") == True
    
def test_hash_table_4(hash_table):
    assert hash_table.contains("red") == False
    
def test_hash_table_5(hash_table):
    assert hash_table.keys() == ['ZONAM', 'AMAZON', 'name']
    
def test_hash_table_6(hash_table):
    assert hash_table.hash("AMAZON") == 434


@pytest.fixture
def hash_table():
    ht = HashTable()
    ht.set('AMAZON', 'AWS')
    ht.set('ZONAM', 'rainy')
    ht.set('name', 'python')
    return ht


