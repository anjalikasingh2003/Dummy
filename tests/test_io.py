from src.utils.io import read_file


def test_read_file(tmp_path):
    f = tmp_path / "abc.txt"
    f.write_text("hello world")
    assert read_file(str(f)) == "hello world"

def test_read_missing_file():
    assert read_file("no_file.txt") is None
