import json


def load_json(file_name):
    with open(f"data/{file_name}.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def dump_json(file_name, data):
    with open(f"data/{file_name}.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def select_items(items, number=False, force=False):
    display = "\n".join([f"{i + 1}. {item}" for i, item in enumerate(items)])
    while True:
        try:
            index = int(input(f"{display}\n>> "))
            if index <= 0:
                raise Exception
            item = items[index - 1]
            return item if not number else index
        except Exception:
            print("----- 입력값이 올바르지 않습니다. -----")
            if not force:
                break
