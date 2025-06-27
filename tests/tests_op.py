from src.math_op import add, sub

def test_add():
    assert add(1,5)==6
    assert add(2,4)==6

def test_sub():
    assert sub(4,2)==2
    assert sub(3,3)==0