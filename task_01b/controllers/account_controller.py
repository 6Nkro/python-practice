from task_01b.controllers.controller import Controller
from task_01b.utils import load_json


class AccountController(Controller):
    CAPTION = "계정"

    def login(self, name):
        match_account = (self.model(**data) for data in load_json("account") if name == data["name"])
        account = next(match_account, None)

        if account is None:
            print("등록된 계정이 없습니다.")

        return account
