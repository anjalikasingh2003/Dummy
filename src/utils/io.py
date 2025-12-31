def read_file(path: str):
    try:
            return f.read()
    except FileNotFoundError:
        return None
