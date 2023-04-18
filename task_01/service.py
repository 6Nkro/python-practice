from datetime import datetime


class MainService:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, account, restaurants):

        restaurant = choice_restaurants(restaurants)

        state = restaurant.get_state()
        if state == "마감":
            return print("영업 시간이 아닙니다.")

        menu = choice_menu(restaurant, state)

        print(f"{menu.price}원이 결제되었습니다.")


def choice_restaurants(restaurants):
    format_list = "\n".join(
        [f"{index + 1}. {r})" for index, r in enumerate(restaurants)]
    )
    output = f"식당을 선택해주세요. (숫자 입력)\n{format_list}\n>> "
    return choice_in_items(restaurants, output)


def choice_menu(restaurant, state):
    menu_list = [menu for menu in restaurant.menu_list if menu.time == state]
    format_list = "\n".join(
        [f"{index + 1}. {menu}" for index, menu in enumerate(menu_list)]
    )
    output = f"[현재 시각 '{datetime.hour}'시] {state}메뉴가 제공됩니다.\n---------- {restaurant.name} 메뉴판 ----------\n{format_list}\n>> "
    return choice_in_items(menu_list, output)


def choice_in_items(items, output):
    while True:
        try:
            choice = int(input(output))
            if choice <= 0:
                raise Exception
            item = items[choice - 1]
        except:
            print("----- 입력값이 올바르지 않습니다. -----\n")
        else:
            return item
