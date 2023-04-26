from abc import ABC
from task_01b.models.model import Model
from task_01b.utils import load_json, dump_json


class Account(Model, ABC):
    SETTINGS = {
        "manuals": [
            {
                "key": "name",
                "type": str
            },
        ],
        "options": [],
        "unique": "name"
    }

    def __init__(self, name, id):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    def save(self):
        dump_json(self)

    @classmethod
    def edit(cls):
        accounts = Resource.get("account")
        account = cls.select_account(accounts, "변경")

        if account is not None:
            old_name = account["name"]
            new_name = input("새로운 아이디를 입력하세요.\n>> ")
            account["name"] = new_name
            dump_json("account", accounts)
            print(f"계정 이름을 \'{old_name}\'에서 \'{new_name}\'으로 변경했습니다.")

    @classmethod
    def delete(cls):
        accounts = Resource.get("account")
        account = cls.select_account(accounts, "삭제")

        if account is not None:
            name = account["name"]
            accounts.remove(account)
            dump_json("account", accounts)
            print(f"\'{name}\' 계정이 삭제되었습니다.")

    @staticmethod
    def select_account(accounts, action):
        account_names = [account["name"] for account in accounts]
        print(f"{action}할 계정을 선택하세요. (번호 입력)")
        name = select_items(account_names)
        account = next((account for account in accounts if name == account["name"]), None)
        return account
