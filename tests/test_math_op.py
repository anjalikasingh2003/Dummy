from src.math_op import add, divide

def test_add():
    assert add(2, 3) == 5

def test_divide_zero():
    assert divide(10, 0) is None
