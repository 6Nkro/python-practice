from task_01b.models import Menu


class MenuController:
    _instance = None
    CAPTION = "메뉴"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
