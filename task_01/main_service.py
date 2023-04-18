from datetime import datetime


class MainService:
    # _instance = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    def __init__(self, account, stores):
        self.account = account
        self.stores = stores

    def choice_store(self):
        stores_to_str = "\n".join([f"{store.id}. {store}" for store in self.stores])
        output = f"식당을 선택해주세요. (숫자 입력)\n{stores_to_str}\n>> "
        return choice_in_items(self.stores, output)

    def choice_meal(self, store):
        meals = store.meals
        meals_to_str = "\n".join([
            f"{index + 1}. [{' / '.join([menu.item for menu in meal.menus])}] {meal.price}원 - {meal.category()}"
            for index, meal in enumerate(meals)
        ])
        output = f"---------- {store} 메뉴판 ----------\n{meals_to_str}\n>> "
        return choice_in_items(meals, output)


def choice_in_items(items, output):
    while True:
        try:
            choice = int(input(output))
            if choice <= 0:
                raise Exception
        except:
            print("----- 입력값이 올바르지 않습니다. -----\n")
        else:
            return items[choice - 1]
