from abc import ABCMeta, abstractmethod

from task_01b.utils import dump_json


class Model(metaclass=ABCMeta):

    @classmethod
    def FILE_NAME(cls):
        return cls.__name__.lower()

    def save(self):
        dump_json(self)

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def delete(self):
        pass
