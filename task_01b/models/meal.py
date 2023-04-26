

class Meal:

    def __init__(self, id, store_id, category_id, price):
        self.id = id
        self.store_id = store_id
        self.category_id = category_id
        self.price = price

    def __str__(self):
        display_menus = " / ".join([menu.name for menu in self.menus()])
        return f"[{display_menus}] {self.price}원 - {self.category()}"

    def menus(self):
        return [menu for menu in Resource.menus if self.id == menu.meal_id]

    def category(self):
        return next(category.name for category in Resource.categories if self.category_id == category.id)

    @classmethod
    def save(cls):
        manuals = [
            Mixin(key="price", type=int)
        ]
        options = [
            Mixin(key="store_id", parent="store"),
            Mixin(key="category_id", items=Resource.categories)
        ]
        unique = None
        cls.save(cls, manuals, options, unique)

    @staticmethod
    def edit():
        print("식사 수정 메소드 호출 [미구현]")

    @staticmethod
    def delete():
        print("식사 삭제 메소드 호출 [미구현]")
