from task_01.classes.mixin import Mixin
from task_01.utils import load_json, dump_json, select_items


class Account:
    TYPE = "계정"
    FILE_NAME = "account"

    def __init__(self, name, id):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def login():
        name = input("아이디를 입력하세요.\n>> ")
        match_account = (Account(**account) for account in load_json("account") if name == account["name"])
        account = next(match_account, None)
        if account is None:
            print("등록된 계정이 없습니다.")
        return account

    @classmethod
    def save(cls):
        manuals = [
            Mixin(key="name", type=str)
        ]
        options = []
        unique = "name"
        Mixin.save(cls, manuals, options, unique)

    @classmethod
    def edit(cls):
        accounts = load_json("account")
        account = cls.select_account(accounts, "변경")

        if account is not None:
            old_name = account["name"]
            new_name = input("새로운 아이디를 입력하세요.\n>> ")
            account["name"] = new_name
            dump_json("account", accounts)
            print(f"계정 이름을 \'{old_name}\'에서 \'{new_name}\'으로 변경했습니다.")

    @classmethod
    def delete(cls):
        accounts = load_json("account")
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
