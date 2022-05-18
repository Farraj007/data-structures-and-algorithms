from stack_queue_brackets.brackets import validate_brackets
import pytest


def test_validate_true():
    
    assert validate_brackets('{}') == True
    assert validate_brackets('{}(){}') == True
    assert validate_brackets('()[[Extra Characters]]') == True
    assert validate_brackets('(){}[[]]') == True
    assert validate_brackets('{}{Code}[Fellows](())') == True
    
def test_validate_false(): 
     
    assert validate_brackets('[({}]') == False
    assert validate_brackets('(](') == False
    assert validate_brackets('{(})') == False
    assert validate_brackets('{') == False
    assert validate_brackets('(') == False
    assert validate_brackets(')') == False
    
def test_validate_error():
    
    with pytest.raises(Exception):
        validate_brackets(5)
