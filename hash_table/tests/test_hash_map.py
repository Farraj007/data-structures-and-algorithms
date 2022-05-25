from hash_table.hashmap import repeated_word
import pytest

text1 = "Once upon a time, there was a brave princess who..."
text2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
text3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

def test_empty_string():
    """test when argument are empty string"""
    with pytest.raises(Exception):
        repeated_word('')
        
    with pytest.raises(Exception):    
        repeated_word('me')  
        
def test_string_1():
    assert repeated_word(text1) == 'a'


def test_string_2():
    assert repeated_word(text2) == "it"


def test_string_3():
    assert repeated_word(text3) == "summer"

