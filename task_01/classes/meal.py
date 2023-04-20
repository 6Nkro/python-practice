from task_01.classes.category import categories


class Meal:

    def __init__(self, menus, id, store_id, category_id, price):
        self.menus = [menu for menu in menus if id == menu.meal_id]
        self.id = id
        self.store_id = store_id
        self.category_id = category_id
        self.price = price
        self.category = next(category.type for category in categories if self.category_id == category.id)

    def __str__(self):
        display_menus = " / ".join([menu.item for menu in self.menus])
        return f"[{display_menus}] {self.price}원 - {self.category}"

    @staticmethod
    def save():
        print("식사 등록 메소드 호출 [미구현]")

    @staticmethod
    def edit():
        print("식사 수정 메소드 호출 [미구현]")

    @staticmethod
    def delete():
        print("식사 삭제 메소드 호출 [미구현]")
