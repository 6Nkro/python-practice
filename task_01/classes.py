from utils import load_json, dump_json


class Account:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    def save(self):
        accounts = load_json("account")
        if self.name in [account["name"] for account in accounts]:
            print("이미 등록된 계정입니다.")
        else:
            self.id = max([account["id"] for account in accounts]) + 1
            dump_json("account", [*accounts, vars(self)])
            print(f"\'{self}\' 계정이 등록되었습니다.")


class Store:
    def __init__(self, meals, services, id, name, close):
        self.meals = [meal for meal in meals if id == meal.store_id]
        self.services = [service for service in services if id == service.store_id]
        self.id = id
        self.name = name
        self.close = close
        self.open = min([service.time_at for service in self.services])

    def __str__(self):
        return self.name


class Meal:
    def __init__(self, menus, id, store_id, category_id, price):
        self.menus = [menu for menu in menus if id == menu.meal_id]
        self.id = id
        self.store_id = store_id
        self.category_id = category_id
        self.price = price

    def category(self):
        return get_category(self.category_id)


class Menu:
    def __init__(self, id, meal_id, item):
        self.id = id
        self.meal_id = meal_id
        self.item = item

    def __str__(self):
        return self.item


class Service:
    def __init__(self, id, store_id, category_id, time_at):
        self.id = id
        self.store_id = store_id
        self.category_id = category_id
        self.time_at = time_at

    def __str__(self):
        return get_category(self.category_id)


class Category:
    def __init__(self, id, type):
        self.id = id
        self.type = type


categories = [Category(**data) for data in load_json("category")]


def get_category(category_id):
    for category in categories:
        if category_id == category.id:
            return category.type
