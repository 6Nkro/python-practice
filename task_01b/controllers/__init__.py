from task_01b.controllers.account_controller import AccountController
from task_01b.controllers.category_controller import CategoryController
from task_01b.controllers.meal_controller import MealController
from task_01b.controllers.menu_controller import MenuController
from task_01b.controllers.service_controller import ServiceController
from task_01b.controllers.store_controller import StoreController
from task_01b.models import Account, Category, Menu, Meal, Service, Store

CONTROLLERS = [
    AccountController(Account),
    CategoryController(Category),
    MenuController(Menu),
    MealController(Meal),
    ServiceController(Service),
    StoreController(Store)
]