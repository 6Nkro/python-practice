class Menu:
    def __init__(self, menu, price, time):
        self.menu = menu
        self.price = price
        self.time = time

    def __str__(self):
        return f"[{' / '.join(self.menu)}] {self.price}원 - {self.time}"
