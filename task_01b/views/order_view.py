from task_01b.controllers import StoreController
from task_01b.models import Store
from task_01b.utils import select_items


class OrderView:

    def __init__(self, account):
        self.account = account

    def render(self):
        print("---------- User Service ----------")
        print("식당을 선택해주세요. (번호 입력)")
        stores = StoreController(Store).find_all()
        store = select_items(stores, force=True)
        meals = store.available_meals()

        if meals is None:
            print("현재 이용 가능한 메뉴가 없습니다.")
        else:
            print("메뉴를 선택해주세요. (번호 입력)")
            meal = select_items(meals, force=True)
            print(f"{self.account}님 {meal.price}원이 결제되었습니다.")