class Menu:
    def __init__(self, id, meal_id, item):
        self.id = id
        self.meal_id = meal_id
        self.item = item

    def __str__(self):
        return self.item

    @staticmethod
    def save():
        print("메뉴 등록 메소드 호출 [미구현]")

    @staticmethod
    def edit():
        print("메뉴 수정 메소드 호출 [미구현]")

    @staticmethod
    def delete():
        print("메뉴 삭제 메소드 호출 [미구현]")
