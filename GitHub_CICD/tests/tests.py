from src.math_Op import add, sub


def test_add():
    assert add(2,2)==4
    assert add(1,10)==11

def test_sub():
    assert sub(2,1)==1
    assert sub (6,2)==4