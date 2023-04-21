# 1. 여러번 생성이 가능하며, 각기 다른 값을 가질 수 있다. 값이 할당되기 전에는 인스턴스를 생성할 수 없다.

class Class01:
    def __init__(self, my_string):
        self.my_string = my_string


a = Class01("aaa")
print("a: ", a, a.my_string)  # a:  <__main__.Class01 object at 0x000001BE9DC35190> aaa
b = Class01("bbb")
print("a: ", a, a.my_string)  # a:  <__main__.Class01 object at 0x000001BE9DC35190> aaa
print("b: ", b, b.my_string)  # b:  <__main__.Class01 object at 0x000001BE9D935010> bbb

print(a is b)  # False


# 2. 오직 한 번만 생성되며, 생성 시 넘겨주는 값은 myString에 할당된다. 해당 값은  프로그램 종료시까지 전체 공유가 된다.

class Class02:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, my_string):
        self.my_string = my_string


a = Class02("aaa")
print("a: ", a, a.my_string)  # a:  <__main__.Class02 object at 0x000001BE9DC355D0> aaa
b = Class02("bbb")
print("a: ", a, a.my_string)  # a:  <__main__.Class02 object at 0x000001BE9DC355D0> bbb
print("b: ", b, b.my_string)  # b:  <__main__.Class02 object at 0x000001BE9DC355D0> bbb

print(a is b)  # True


# 3. 오직 한 번만 생성되며, 생성 시 넘겨주는 값은 myString에 할당된다. 해당 값은  프로그램 종료시까지 전체 공유가 되며, 두 번 다시 변경할 수 없다.


class Class03:
    _instance = None
    _exist = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, my_string):
        if not self._exist:
            self.my_string = my_string
            self._exist = True


a = Class03("aaa")
print("a: ", a, a.my_string)  # a:  <__main__.Class03 object at 0x000001BE9DC35190> aaa
b = Class03("bbb")
print("a: ", a, a.my_string)  # a:  <__main__.Class03 object at 0x000001BE9DC35190> aaa
print("b: ", b, b.my_string)  # b:  <__main__.Class03 object at 0x000001BE9DC35190> aaa

print(a is b)  # True
