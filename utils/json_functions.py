import json

def get_data_from_json_file(path) -> json:
    f = open(path)
    data = json.load(f)
    f.close()
    return data