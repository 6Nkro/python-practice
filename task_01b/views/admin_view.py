from task_01b.controllers import CONTROLLERS
from task_01b.utils import select_items, load_json, dump_json


class AdminView:

    @classmethod
    def render(cls):
        controller_map = {controller.CAPTION: controller for controller in CONTROLLERS}
        print("관리할 항목을 선택하세요. (번호 입력)")
        caption = select_items(list(controller_map.keys()), force=True)
        controller = controller_map[caption]

        print(f"{caption}에 대한 작업을 선택하세요. (번호 입력)")
        action = select_items(["등록", "수정", "삭제"], force=True)
        controller.admin(action)

    @classmethod
    def insert(cls, model):
        data = load_json(model.FILE_NAME())
        manuals, options, unique = model.SETTINGS.values()

        required = {}
        for manual in manuals:
            key, _type, _range = (manual.get("key", None), manual.get("type", None), manual.get("range", None))
            try:
                required[key] = _type(input(f"[{key}] 값을 입력하세요. [{_type.__name__}] {_range}\n>> "))
                if _range and not required[key] in range(_range[0], _range[1] + 1):
                    raise Exception
            except Exception:
                print("----- 입력값이 올바르지 않습니다. -----")
                return
            if key == unique and any(required[key] == row[key] for row in data):
                print(f"[{key}: {required[key]}] 중복된 값이 존재합니다.")
                return

        for option in options:
            key = f"{option}_id"
            items = load_json(option)
            print(f"[{key}] 값을 선택하세요. (번호 입력)")
            required[key] = select_items(items, number=True, force=True)

        id = max([row["id"] for row in data]) + 1
        model(id, **required).save()
