class DBClient:
    def __init__(self):
        self.db = {}  # simple in-memory mock DB

    def insert(self, key, value):
        # No validation → tests will catch errors
        self.db[key] = value

    def get(self, key):
        return self.db[key]   # will throw KeyError
