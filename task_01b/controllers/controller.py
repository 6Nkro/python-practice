from task_01b.utils import load_json


class Controller:
    _instances = {}
    CAPTION = None

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    def __init__(self, model):
        self.model = model

    def post(self, url, params):
        url_map = {
            "등록": lambda: self.insert(params),
            "수정": lambda: self.update(params),
            "삭제": lambda: self.delete(params)
        }
        return url_map[url]()

    def requirements(self):
        return {
            "data": self.model.find_all(),
            "settings": self.model.SETTINGS.values()
        }

    def find_all(self):
        return self.model.find_all()

    def insert(self, params):
        data = load_json(self.model.file_name())
        id = max([row["id"] for row in data]) + 1
        result = self.model(id, **params).insert()
        return f"{self.CAPTION} 등록 완료" if result == 201 else "Error!"

    def update(self, params):
        return f"{self.CAPTION} update 호출"

    def delete(self, params):
        return f"{self.CAPTION} delete 호출"
