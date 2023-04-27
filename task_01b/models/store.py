from datetime import datetime

from task_01b.models import Service, Meal
from task_01b.models.model import Model
from task_01b.utils import load_json


class Store(Model):
    SETTINGS = {
        "manuals": ["name", "close"],
        "options": [],
        "unique": None
    }

    def __init__(self, id, name, close):
        self.id = id
        self.name = name
        self.close = int(close)

    def __str__(self):
        display_services = " ".join([str(service) for service in self.services()])
        return f"{self.name} [{display_services} 마감: {self.close}시]"

    def meals(self):
        return [Meal(**data) for data in load_json("meal") if self.id == data["store_id"]]

    def services(self):
        return [Service(**data) for data in load_json("service") if self.id == data["store_id"]]

    def open(self):
        return min([service.time_at for service in self.services()])

    def available_meals(self):
        curr_hour = datetime.now().hour
        if curr_hour < self.open() or curr_hour >= self.close:
            return None

        category_id = next(service.category_id for service in self.services() if curr_hour >= service.time_at)
        return [meal for meal in self.meals() if meal.category_id == category_id]
