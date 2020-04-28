import json

def __read_file(loc: str):
    """
    This function reads a JSON file and returns an object.
    """
    with open(loc, 'r') as f:
        return json.loads(f.read())

def get_obj(loc: str):
    """
    This function returns a Python object based on the contents of a JSON file.
    """
    return __read_file(loc)