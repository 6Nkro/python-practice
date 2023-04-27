from task_01b.controllers import CONTROLLERS
from task_01b.utils import select_items, load_json


class AdminView:

    @classmethod
    def render(cls):
        print("관리할 항목을 선택하세요. (번호 입력)")
        controller = cls.get_controller()

        print(f"{controller.CAPTION}에 대한 작업을 선택하세요. (번호 입력)")
        url = cls.get_url()
        params = cls.get_params(controller)

        if params is not None:
            res = controller.post(url, params)
            print(res)

    @classmethod
    def get_controller(cls):
        controller_map = {controller.CAPTION: controller for controller in CONTROLLERS}
        caption = select_items(list(controller_map.keys()), force=True)
        return controller_map[caption]

    @classmethod
    def get_url(cls):
        return select_items(["등록", "수정", "삭제"], force=True)

    @classmethod
    def get_params(cls, controller):
        res = controller.requirements()
        data = res.get("data")
        manuals, options, unique = res.get("settings")

        params = {}
        for key in manuals:
            params[key] = input(f"[{key}] 값을 입력하세요.\n>> ")
            if key == unique and any(params[key] == row[key] for row in data):
                print(f"[{key}: {params[key]}] 중복된 값이 존재합니다.")
                return

        for option in options:
            key = f"{option}_id"
            items = load_json(option)
            print(f"[{key}] 값을 선택하세요. (번호 입력)")
            params[key] = select_items(items, number=True, force=True)

        return params
