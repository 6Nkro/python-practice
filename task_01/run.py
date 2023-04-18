from classes import Service, Menu, Meal, Store, Account
from main_service import MainService
from utils import load_json


services = [Service(**data) for data in load_json("service")]
menus = [Menu(**item) for item in load_json("menu")]
meals = [Meal(menus, **data) for data in load_json("meal")]
stores = [Store(meals, services, **data) for data in load_json("store")]

account = Account(1, input("사용자 아이디를 입력하세요.\n>> "))
main = MainService(account, stores)

store = main.choice_store()
meal = main.choice_meal(store)
print(f"{meal.price}원이 결제되었습니다.")
