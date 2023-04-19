from task_01.utils import load_json


class Category:
    def __init__(self, id, type):
        self.id = id
        self.type = type


categories = [Category(**data) for data in load_json("category")]
