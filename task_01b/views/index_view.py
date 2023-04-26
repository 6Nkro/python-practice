from task_01b.controllers.account_controller import AccountController
from task_01b.utils import select_items
from task_01b.views.admin_view import AdminView
from task_01b.views.order_view import OrderView


class IndexView:

    @staticmethod
    def render():
        print("작업을 선택하세요. (번호 입력)")
        action = select_items(["로그인", "회원가입"], force=True)

        if action == "로그인":
            name = input("아이디를 입력하세요.\n>> ")
            account = AccountController.login(name)
        elif action == "회원가입":
            AccountController.signup()

        if account and account.name == "admin":
            AdminView().render()
        elif account:
            OrderView(account).render()
