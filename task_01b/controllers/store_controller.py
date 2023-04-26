from task_01b.models import Store


class StoreController:
    _instance = None
    CAPTION = "식당"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
