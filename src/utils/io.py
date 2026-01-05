def read_file(path: str):
++ b//home/runner/work/Dummy/Dummy/src/utils/io.py
    try:
            return f.read()
    except FileNotFoundError:
        return None
# hfu