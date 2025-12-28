from src.utils.io import read_file

def test_file():
    assert read_file("hello.txt") == "data"
