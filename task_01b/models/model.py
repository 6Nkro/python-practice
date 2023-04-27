from task_01b.utils import dump_json, load_json


class Model:

    @classmethod
    def file_name(cls):
        return cls.__name__.lower()

    @classmethod
    def find_all(cls):
        return load_json(cls.file_name())

    def insert(self):
        try:
            data = load_json(self.file_name())
            data.append(vars(self))
            dump_json(self.file_name(), data)
            return 201
        except Exception:
            return 400

    def update(self):
        pass

    def delete(self):
        pass
