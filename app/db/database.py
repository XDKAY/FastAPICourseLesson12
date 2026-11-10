from .models.user import UserModel

__all__ = ("Database",)


class Database:

    __MODEL = UserModel
    __VAULT: list[__MODEL] = []

    def __init__(self) -> None:
        self._database = self.__VAULT

    def get_data(self) -> list['Database.__MODEL']:
        return self._database

    def add_value(self, value: 'Database.__MODEL') -> None:
        self._database.append(value)
