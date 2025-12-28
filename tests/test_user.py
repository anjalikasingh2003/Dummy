from src.user import load_user

def test_user():
    assert load_user(1) == 10