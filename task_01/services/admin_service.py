from task_01.classes.account import Account
from task_01.classes.meal import Meal
from task_01.classes.menu import Menu
from task_01.classes.service import Service
from task_01.classes.store import Store
from task_01.utils import select_items


class AdminService:

    def __init__(self):
        self.category_map = {
            "계정": Account,
            "식당": Store,
            "식사": Meal,
            "메뉴": Menu,
            "서비스": Service
        }
        self.action_map = {
            "등록": lambda x: x.save(),
            "수정": lambda x: x.edit(),
            "삭제": lambda x: x.delete()
        }

    def process(self):
        self.run_action(*self.select_action())

    def select_action(self):
        print("관리할 항목을 선택하세요. (번호 입력)")
        categories = list(self.category_map.keys())
        selected_category = select_items(categories, force=True)

        print(f"{selected_category}에 대한 작업을 선택하세요. (번호 입력)")
        actions = list(self.action_map.keys())
        selected_action = select_items(actions, force=True)

        return selected_category, selected_action

    def run_action(self, category, action):
        _class = self.category_map[category]
        _action = self.action_map[action]
        _action(_class)
