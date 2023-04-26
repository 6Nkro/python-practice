from task_01b.models import Service


class ServiceController:
    _instance = None
    CAPTION = "서비스"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
