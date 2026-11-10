from abc import ABC, abstractmethod
from typing import Optional

from app.core.schemes.user import UserRequestScheme, UserResponseScheme
from app.db.database import Database
from app.db.models.user import UserModel

__all__ = ("AbstractUserRepository", "UserRepository",)


class AbstractUserRepository(ABC):

    __MODEL = None

    @abstractmethod
    def add(self, user: UserRequestScheme) -> UserResponseScheme:
        ...

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[UserResponseScheme]:
        ...

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[UserResponseScheme]:
        ...

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UserResponseScheme]:
        ...


class UserRepository(AbstractUserRepository):

    __MODEL = UserModel

    def __init__(self, database: Database) -> None:
        self._database = database

    def add(self, user: UserRequestScheme) -> UserResponseScheme:
        user_model = self.__MODEL.model_validate(user)
        self._database.add_value(user_model)
        return UserResponseScheme.model_validate(user_model)

    def get_by_id(self, id: str) -> Optional[UserResponseScheme]:
        for user in self._database.get_data():
            if user.id == id:
                return UserResponseScheme.model_validate(user)

        return None

    def get_by_username(self, username: str) -> Optional[UserResponseScheme]:
        for user in self._database.get_data():
            if user.username == username:
                return UserResponseScheme.model_validate(user)

        return None

    def get_by_email(self, email: str) -> Optional[UserResponseScheme]:
        for user in self._database.get_data():
            if user.email == email:
                return UserResponseScheme.model_validate(user)

        return None
