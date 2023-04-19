from task_01.utils import load_json, dump_json, select_items


class Account:
    def __init__(self, name, id=None):
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

    @staticmethod
    def save():
        name = input("등록할 아이디를 입력하세요.\n>> ")
        accounts = load_json("account")

        if any(name == account["name"] for account in accounts):
            print("이미 등록된 계정입니다.")
        else:
            id = max([account["id"] for account in accounts]) + 1
            accounts.append({"id": id, "name": name})
            dump_json("account", accounts)
            print(f"\'{name}\' 계정이 등록되었습니다.")

    @staticmethod
    def edit():
        accounts = load_json("account")
        account = select_account(accounts, "변경")

        if account is not None:
            old_name = account["name"]
            new_name = input("새로운 아이디를 입력하세요.\n>> ")
            account["name"] = new_name
            dump_json("account", accounts)
            print(f"계정 이름을 \'{old_name}\'에서 \'{new_name}\'으로 변경했습니다.")

    @staticmethod
    def delete():
        accounts = load_json("account")
        account = select_account(accounts, "삭제")

        if account is not None:
            name = account["name"]
            accounts.remove(account)
            dump_json("account", accounts)
            print(f"\'{name}\' 계정이 삭제되었습니다.")


def select_account(accounts, action):
    account_names = [account["name"] for account in accounts]
    print(f"{action}할 계정을 선택하세요. (번호 입력)")
    name = select_items(account_names)
    account = next((account for account in accounts if name == account["name"]), None)
    return account
