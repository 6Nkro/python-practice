from task_01.classes.account import Account
from task_01.classes.meal import Meal
from task_01.classes.menu import Menu
from task_01.classes.service import Service
from task_01.classes.store import Store
from task_01.utils import load_json


services = [Service(**data) for data in load_json("service")]
menus = [Menu(**item) for item in load_json("menu")]
meals = [Meal(menus, **data) for data in load_json("meal")]
stores = [Store(meals, services, **data) for data in load_json("store")]
accounts = [Account(**data) for data in load_json("account")]
