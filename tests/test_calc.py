from src.my_test import divide
from src.calc import divide_l
def test_divide_by_zero():
    print("testingn")
    a= divide(10, 2) == 5
    b= divide_l(10, 2) == 5