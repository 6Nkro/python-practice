from task_01b.models import Category
class CategoryController:
    _instance = None
    CAPTION = "카테고리"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
