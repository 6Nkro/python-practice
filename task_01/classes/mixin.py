from task_01.utils import load_json, dump_json, select_items


class Mixin:

    def __init__(self, key, type=None, range=None, items=None):
        self.key = key
        self.type = type
        self.range = range
        self.items = items

    @staticmethod
    def save(entity, manuals, options, unique):
        data = load_json(entity.FILE_NAME)

        required = {}
        for manual in manuals:
            key, type, _range = (manual.key, manual.type, manual.range)
            try:
                required[key] = type(input(f"[{key}] 값을 입력하세요. [{type.__name__}] {_range}\n>> "))
                if _range and not required[key] in range(_range[0], _range[1] + 1):
                    raise Exception
            except Exception:
                print("----- 입력값이 올바르지 않습니다. -----")
                return
            if key == unique and any(required[key] == row[key] for row in data):
                print(f"[{key}: {required[key]}] 중복된 값이 존재합니다.")
                return

        for option in options:
            key, items = (option.key, option.items)
            print(f"[{key}] 값을 선택하세요. (번호 입력)")
            required[key] = select_items(items, number=True, force=True)

        id = max([row["id"] for row in data]) + 1
        data.append({"id": id, **required})
        dump_json(entity.FILE_NAME, data)
        print(f"[{entity.TYPE}] 등록을 완료했습니다.")

    @staticmethod
    def edit():
        pass

    @staticmethod
    def delete():
        pass
