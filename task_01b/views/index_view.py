from task_01b.controllers.account_controller import AccountController
from task_01b.models import Account
from task_01b.utils import select_items
from task_01b.views.admin_view import AdminView
from task_01b.views.order_view import OrderView


class IndexView:

    def __init__(self):
        self.account = None
        self.account_controller = AccountController(Account)

    def render(self):
        print("작업을 선택하세요. (번호 입력)")
        action = select_items(["로그인", "회원가입"], force=True)

        if action == "로그인":
            name = input("아이디를 입력하세요.\n>> ")
            self.account = self.account_controller.login(name)
        elif action == "회원가입":
            params = AdminView().get_params(self.account_controller)
            if params is not None:
                res = self.account_controller.insert(params)
                print(res)

        if self.account and self.account.name == "admin":
            AdminView().render()
        elif self.account:
            OrderView(self.account).render()
