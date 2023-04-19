from classes import Service, Menu, Meal, Store, Account
from main_service import MainService, choice_in_items, available_meals, choice_in_stores, choice_in_meals
from admin_service import AdminService
from utils import load_json

services = [Service(**data) for data in load_json("service")]
menus = [Menu(**item) for item in load_json("menu")]
meals = [Meal(menus, **data) for data in load_json("meal")]
stores = [Store(meals, services, **data) for data in load_json("store")]
accounts = [Account(**data) for data in load_json("account")]

while True:
    print("----------Task_01 ----------")
    action = choice_in_items(["로그인", "회원가입"])
    name = input("아이디를 입력하세요.\n>> ")
    account = MainService.login(name)

    if action == "회원가입":
        Account(name).save()
    elif name == "admin":
        print("---------- 관리자 모드 ----------")
        categories = list(AdminService.category_map.keys())
        selected_category = choice_in_items(categories)

        actions = list(AdminService.action_map.keys())
        selected_action = choice_in_items(actions)

        name = input(f"* {selected_action} {selected_category} 입력 *\n>> ")
        AdminService.action(selected_category, selected_action, name)
    elif account is None:
        print("등록되지 않은 ID입니다.")
    else:
        print("식당을 선택해주세요. (번호 입력)")
        store = choice_in_stores(stores)
        meals = available_meals(store)
        if meals is None:
            print("영업시간이 아닙니다.")
        else:
            print("메뉴를 선택해주세요. (번호 입력)")
            meal = choice_in_meals(available_meals(store))
            print(f"{meal.price}원이 결제되었습니다.")
