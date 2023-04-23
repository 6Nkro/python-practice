from task_01.classes.mixin import Mixin
from task_01.classes.resource import Resource


class Menu:
    TYPE = "메뉴"
    FILE_NAME = "menu"

    def __init__(self, id, meal_id, name):
        self.id = id
        self.meal_id = meal_id
        self.name = name

    def __str__(self):
        return self.name

    @classmethod
    def save(cls):
        manuals = [
            Mixin(key="name", type=str)
        ]
        options = [
            Mixin(key="meal_id", items=Resource.meals)
        ]
        unique = None
        Mixin.save(cls, manuals, options, unique)

    @staticmethod
    def edit():
        print("메뉴 수정 메소드 호출 [미구현]")

    @staticmethod
    def delete():
        print("메뉴 삭제 메소드 호출 [미구현]")
