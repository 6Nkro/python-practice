

class Category:
    SAVE_SETTING = {
        "manuals": [
            {
                "key": "name",
                "type": str
             }
        ],
        "options": [],
        "unique": "name"
    }

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    @classmethod
    def save(cls):
        Mixin.save(cls)

    @staticmethod
    def edit():
        print("서비스 수정 메소드 호출 [미구현]")

    @staticmethod
    def delete():
        print("서비스 삭제 메소드 호출 [미구현]")
