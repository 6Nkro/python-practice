from task_01b.models import Menu
from task_01b.models.model import Model
from task_01b.utils import load_json


class Meal(Model):
    SETTINGS = {
        "manuals": ["price"],
        "options": ["store", "category"],
        "unique": None
    }

    def __init__(self, id, store_id, category_id, price):
        self.id = id
        self.store_id = store_id
        self.category_id = category_id
        self.price = price

    def __str__(self):
        display_menus = " / ".join([menu.name for menu in self.menus()])
        return f"[{display_menus}] {self.price}원 - {self.category()}"

    def menus(self):
        return [Menu(**data) for data in load_json("menu") if self.id == data["meal_id"]]

    def category(self):
        return next(data["name"] for data in load_json("category") if self.category_id == data["id"])
