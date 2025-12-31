from src.user import create_user

def test_create_user():
    u = create_user("Anjalika", 22)

    assert u["name"] == "Anjalika"
    assert u["age"] == 22
