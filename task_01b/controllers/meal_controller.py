from task_01b.models import Meal


class MealController:
    _instance = None
    CAPTION = "식사"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
