from task_01.classes.mixin import Mixin
from task_01.classes.resource import Resource


class Service:
    TYPE = "서비스"
    FILE_NAME = "service"

    def __init__(self, id, store_id, category_id, time_at):
        self.id = id
        self.store_id = store_id
        self.category_id = category_id
        self.time_at = time_at

    def __str__(self):
        return f"{self.category()}: {self.time_at}시"

    def category(self):
        return next(category.name for category in Resource.categories if self.category_id == category.id)

    @classmethod
    def save(cls):
        manuals = [
            Mixin(key="time_at", type=int, range=(0, 23))
        ]
        options = [
            Mixin(key="store_id", items=Resource.stores),
            Mixin(key="category_id", items=Resource.categories)
        ]
        unique = None
        Mixin.save(cls, manuals, options, unique)

    @staticmethod
    def edit():
        print("서비스 수정 메소드 호출 [미구현]")

    @staticmethod
    def delete():
        print("서비스 삭제 메소드 호출 [미구현]")
