from task_01.classes.account import Account
from task_01.classes.category import Category
from task_01.classes.meal import Meal
from task_01.classes.menu import Menu
from task_01.classes.service import Service
from task_01.classes.store import Store
from task_01.utils import select_items


class AdminService:
    ENTITIES = [Account, Store, Meal, Menu, Service, Category]
    ACTION_MAP = {
        "등록": lambda entity: entity.save(),
        "수정": lambda entity: entity.edit(),
        "삭제": lambda entity: entity.delete()
    }

    @classmethod
    def process(cls):
        entity_type, action = cls.select_entity()
        entity = next(entity for entity in cls.ENTITIES if entity.TYPE == entity_type)
        cls.ACTION_MAP[action](entity)

    @classmethod
    def select_entity(cls):
        print("관리할 항목을 선택하세요. (번호 입력)")
        entity_types = [entity.TYPE for entity in cls.ENTITIES]
        selected_type = select_items(entity_types, force=True)

        print(f"{selected_type}에 대한 작업을 선택하세요. (번호 입력)")
        actions = list(cls.ACTION_MAP.keys())
        selected_action = select_items(actions, force=True)

        return selected_type, selected_action
