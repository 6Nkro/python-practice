from task_01.classes.account import Account
from task_01.services.admin_service import AdminService
from task_01.services.user_service import UserService
from task_01.utils import select_items


class MainService:

    def __init__(self):
        self.account = None

    def process(self):
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
