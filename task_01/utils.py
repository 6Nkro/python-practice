import json


def load_json(file_name):
    with open(f"data/{file_name}.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def dump_json(file_name, data):
    with open(f"data/{file_name}.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


def select_items(items, force=False):
    display = "\n".join([f"{i + 1}. {item}" for i, item in enumerate(items)])
    while True:
        try:
            index = int(input(f"{display}\n>> "))
            if index <= 0:
                raise Exception
            return items[index - 1]
        except Exception:
            print("----- 입력값이 올바르지 않습니다. -----")
            if not force:
                break
