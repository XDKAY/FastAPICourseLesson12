from typing import Annotated

from fastapi import Depends

from app.core.repositories.user import UserRepository
from app.core.services.user import UserService
from app.db.database import Database

__all__ = ("UserServiceDep", )


def get_user_repository() -> UserRepository:
    return UserRepository(Database())


UserRepoDep = Annotated[UserRepository, Depends(get_user_repository)]


def get_user_service(user_repository: UserRepoDep) -> UserService:
    return UserService(user_repository)


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
