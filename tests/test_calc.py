from src.my_test import divide

def test_divide_by_zero():
    print("testing")
    assert divide(10, 2) == 5