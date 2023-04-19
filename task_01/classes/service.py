from task_01.classes.category import categories


class Service:

    def __init__(self, id, store_id, category_id, time_at):
        self.id = id
        self.store_id = store_id
        self.category_id = category_id
        self.time_at = time_at
        self.category = next(category.type for category in categories if self.category_id == category.id)

    def __str__(self):
        return f"{self.category}: {self.time_at}시"

    @staticmethod
    def save():
        print("서비스 등록 메소드 호출 [미구현]")

    @staticmethod
    def edit():
        print("서비스 수정 메소드 호출 [미구현]")

    @staticmethod
    def delete():
        print("서비스 삭제 메소드 호출 [미구현]")
