class Controller:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    def admin(self, action):
        action_map = {
            "등록": lambda: self.insert(),
            "수정": lambda: self.update(),
            "삭제": lambda: self.delete()
        }
        action_map[action]()

