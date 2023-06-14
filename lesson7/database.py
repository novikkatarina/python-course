import json


def read_data():
    path = 'db.json'
    with open(path, 'r') as f:
        res = json.loads(f.read())`
        return res


def save_data(objects):
    path = 'db.json'
    with open(path, 'w') as f:
        s = json.dumps(objects)
        f.write(s)
