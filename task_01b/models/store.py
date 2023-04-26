from datetime import datetime


class Store:

    def __init__(self, id, name, close):
        self.id = id
        self.name = name
        self.close = close

    def __str__(self):
        display_services = " ".join([str(service) for service in self.services()])
        return f"{self.name} [{display_services} 마감: {self.close}시]"

    def meals(self):
        return [meal for meal in Resource.meals if self.id == meal.store_id]

    def services(self):
        return [service for service in Resource.services if self.id == service.store_id]

    def open(self):
        return min([service.time_at for service in self.services()])

    def available_meals(self):
        curr_hour = datetime.now().hour
        if curr_hour < self.open() or curr_hour >= self.close:
            return None

        category_id = next(service.category_id for service in self.services() if curr_hour >= service.time_at)
        return [meal for meal in self.meals() if meal.category_id == category_id]

    @classmethod
    def save(cls):
        manuals = [
            Mixin(key="name", type=str),
            Mixin(key="close", type=int, range=(0, 23))
        ]
        options = []
        unique = "name"
        Mixin.save(cls, manuals, options, unique)

    @staticmethod
    def edit():
        print("식당 수정 메소드 호출 [미구현]")

    @staticmethod
    def delete():
        print("식당 삭제 메소드 호출 [미구현]")
