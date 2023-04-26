from task_01b.controllers.controller import Controller
from task_01b.models import Account
from task_01b.utils import load_json


class AccountController(Controller):
    CAPTION = "계정"


    @classmethod
    def login(cls, name):
        match_account = (Account(**data) for data in load_json("account") if name == data["name"])
        account = next(match_account, None)

        if account is None:
            print("등록된 계정이 없습니다.")

        return account

    def signup(self):
        pass