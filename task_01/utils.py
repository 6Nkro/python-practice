import json


def load_json(file_name):
    with open(f"data/{file_name}.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
