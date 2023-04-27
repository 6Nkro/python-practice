from task_01b.models.model import Model


class Category(Model):
    SETTINGS = {
        "manuals": ["name"],
        "options": [],
        "unique": "name"
    }

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name
