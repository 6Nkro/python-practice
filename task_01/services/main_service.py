from task_01.classes.account import Account
from task_01.classes.category import Category
from task_01.classes.meal import Meal
from task_01.classes.menu import Menu
from task_01.classes.service import Service
from task_01.classes.store import Store
from task_01.classes.resource import Resource
from task_01.services.admin_service import AdminService
from task_01.services.user_service import UserService
from task_01.utils import select_items, load_json


class MainService:

    def __init__(self):
        self.account = None

    def process(self):
        self.load_data()
        print("작업을 선택하세요. (번호 입력)")
        action = select_items(["로그인", "회원가입"], force=True)

        if action == "로그인":
            self.account = Account.login()
        elif action == "회원가입":
            Account.save()

        if self.account and self.account.name == "admin":
            AdminService().process()
        elif self.account:
            UserService(self.account).process()

    @staticmethod
    def load_data():
        Resource.services = [Service(**data) for data in load_json("service")]
        Resource.menus = [Menu(**data) for data in load_json("menu")]
        Resource.meals = [Meal(**data) for data in load_json("meal")]
        Resource.stores = [Store(**data) for data in load_json("store")]
        Resource.accounts = [Account(**data) for data in load_json("account")]
        Resource.categories = [Category(**data) for data in load_json("category")]
