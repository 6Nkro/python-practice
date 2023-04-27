from task_01b.models.model import Model
from task_01b.utils import load_json


class Service(Model):
    SETTINGS = {
        "manuals": ["time_at"],
        "options": ["store", "category"],
        "unique": None
    }

    def __init__(self, id, store_id, category_id, time_at):
        self.id = id
        self.store_id = store_id
        self.category_id = category_id
        self.time_at = int(time_at)

    def __str__(self):
        return f"{self.category()}: {self.time_at}시"

    def category(self):
        return next(data["name"] for data in load_json("category") if self.category_id == data["id"])
