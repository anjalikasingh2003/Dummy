def read_file(path: str):
++ b/src/utils/io.py
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None
