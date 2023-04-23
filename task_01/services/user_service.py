from task_01.classes.resource import Resource
from task_01.utils import select_items


class UserService:

    def __init__(self, account):
        self.account = account

    @classmethod
    def process(cls):
        print("---------- User Service ----------")
        print("식당을 선택해주세요. (번호 입력)")
        store = select_items(Resource.stores, force=True)
        meals = store.available_meals()

        if meals is None:
            print("현재 이용 가능한 메뉴가 없습니다.")
        else:
            print("메뉴를 선택해주세요. (번호 입력)")
            meal = select_items(meals, force=True)
            print(f"{meal.price}원이 결제되었습니다.")