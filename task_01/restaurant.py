from datetime import datetime

from task_01.menu import Menu


class Restaurant:
    def __init__(self, name, menu_list, service_time=None):
        self.name = name
        self.menu_list = [Menu(**menu) for menu in menu_list]
        self.service_time = service_time if service_time is not None else {
            "아침": 8,
            "점심": 13,
            "저녁": 18,
            "마감": 20,
        }

    def __str__(self):
        return f"{self.name} ({self.service_time['아침']}시~{self.service_time['마감']}시"

    def get_state(self):
        state = "마감"
        for key, value in self.service_time.items():
            if value <= datetime.now().hour:
                state = key
        return state
