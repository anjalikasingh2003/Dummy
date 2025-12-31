from src.db.client import DBClient

def test_insert_and_get():
    db = DBClient()
    db.insert("u1", {"name": "John"})

    result = db.get("u1")
    assert result["name"] == "John"
