from classes import Account, Store


class AdminService:
    category_map = {
        "계정": Account,
        "식당": Store
    }

    action_map = {
        "등록": lambda x: x.save(),
        "수정": lambda x: x.edit(),
        "삭제": lambda x: x.delete()
    }

    @staticmethod
    def action(category, action, name):
        _class = AdminService.category_map[category]
        _instance = _class(name)
        save = AdminService.action_map[action]
        save(_instance)
