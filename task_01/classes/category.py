from task_01.classes.mixin import Mixin


class Category:
    TYPE = "카테고리"
    FILE_NAME = "category"

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    @classmethod
    def save(cls):
        manuals = [
            Mixin(key="name", type=str)
        ]
        options = []
        unique = "name"
        Mixin.save(cls, manuals, options, unique)

    @staticmethod
    def edit():
        print("서비스 수정 메소드 호출 [미구현]")

    @staticmethod
    def delete():
        print("서비스 삭제 메소드 호출 [미구현]")
