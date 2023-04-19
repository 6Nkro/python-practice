from datetime import datetime

from classes import Account
from utils import load_json


class MainService:

    @staticmethod
    def login(name):
        for account in load_json("account"):
            if name == account["name"]:
                return Account(**account)
        return None


def choice(func):
    def wrapper(items):
        display = f"{func(items)}\n>> "
        while True:
            index = 0
            try:
                index = int(input(display))
                if index <= 0:
                    raise Exception
                item = items[index - 1]
            except Exception:
                print("----- 입력값이 올바르지 않습니다. -----")
                print(f"index: {index}, len(items): {len(items)}\n")
            else:
                return item

    return wrapper


@choice
def choice_in_items(items, extra=""):
    return "\n".join([f"{index + 1}. {item} {extra}" for index, item in enumerate(items)])


@choice
def choice_in_stores(stores):
    return "\n".join([
        f"{store.id}. {store} [{display_services(store.services)} 마감: {store.close}시]"
        for store in stores
    ])


@choice
def choice_in_meals(meals):
    return "\n".join([
        f"{index + 1}. [{display_menus(meal.menus)}] {meal.price}원 - {meal.category()}"
        for index, meal in enumerate(meals)
    ])


def display_services(services):
    return " ".join([
        f"{service}: {service.time_at}시"
        for service in services
    ])


def display_menus(menus):
    return " / ".join([menu.item for menu in menus])


def available_meals(store):
    curr_hour = datetime.now().hour
    if curr_hour < store.open or curr_hour >= store.close:
        return None

    for service in store.services:
        if curr_hour >= service.time_at:
            category_id = service.category_id
    return [meal for meal in store.meals if meal.category_id == category_id]
