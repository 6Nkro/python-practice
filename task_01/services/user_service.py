from task_01.resource import stores
from task_01.utils import select_items


class UserService:

    def __init__(self, account):
        self.account = account

    def process(self):
        print("---------- User Service ----------")
        store = self.select_store()
        meals = store.available_meals()

        if meals is None:
            print("영업시간이 아닙니다.")
        else:
            meal = self.select_meal(meals)
            print(f"{meal.price}원이 결제되었습니다.")

    def select_store(self):
        print("식당을 선택해주세요. (번호 입력)")
        store = select_items(stores, force=True)
        return store

    def select_meal(self, meals):
        print("메뉴를 선택해주세요. (번호 입력)")
        meal = select_items(meals, force=True)
        return meal
