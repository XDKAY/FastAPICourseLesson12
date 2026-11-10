from typing import Optional

from app.core.repositories.user import AbstractUserRepository
from app.core.schemes.user import UserRequestScheme, UserResponseScheme

__all__ = ("UserService", )


class UserService:
    def __init__(self, repository: AbstractUserRepository) -> None:
        self._repository = repository

    def add(self, user: UserRequestScheme) -> UserResponseScheme:
        return self._repository.add(user)

    def get_by_id(self, id: str) -> Optional[UserResponseScheme]:
        return self._repository.get_by_id(id)

    def get_by_username(self, username: str) -> Optional[UserResponseScheme]:
        return self._repository.get_by_username(username)

    def get_by_email(self, email: str) -> Optional[UserResponseScheme]:
        return self._repository.get_by_email(email)
