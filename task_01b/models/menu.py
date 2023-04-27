from task_01b.models.model import Model


class Menu(Model):
    SETTINGS = {
        "manuals": ["name"],
        "options": ["meal"],
        "unique": None
    }

    def __init__(self, id, meal_id, name):
        self.id = id
        self.meal_id = meal_id
        self.name = name

    def __str__(self):
        return self.name
