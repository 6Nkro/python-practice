from datetime import datetime


class Store:
    def __init__(self, meals, services, id, name, close):
        self.meals = [meal for meal in meals if id == meal.store_id]
        self.services = [service for service in services if id == service.store_id]
        self.id = id
        self.name = name
        self.close = close
        self.open = min([service.time_at for service in self.services])

    def __str__(self):
        display_services = " ".join([str(service) for service in self.services])
        return f"{self.name} [{display_services} 마감: {self.close}시]"

    def available_meals(self):
        curr_hour = datetime.now().hour
        if curr_hour < self.open or curr_hour >= self.close:
            return None

        category_id = next(service.category_id for service in self.services if curr_hour >= service.time_at)
        return [meal for meal in self.meals if meal.category_id == category_id]

    @staticmethod
    def save():
        print("식당 등록 메소드 호출 [미구현]")

    @staticmethod
    def edit():
        print("식당 수정 메소드 호출 [미구현]")

    @staticmethod
    def delete():
        print("식당 삭제 메소드 호출 [미구현]")