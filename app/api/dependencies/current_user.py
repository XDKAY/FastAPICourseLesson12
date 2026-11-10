from typing import Optional, Annotated
from fastapi import Cookie, Depends, HTTPException, status

from .database import UserServiceDep
from app.core.schemes.user import UserResponseScheme
from app.core.security.signature import signature

__all__ = ("CurrentUserDep", )


def get_current_user(
    user_service: UserServiceDep,
    session_token: Optional[str] = Cookie(default=None)
) -> UserResponseScheme:

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Пользватель не авторизован в системе"
    )

    if not session_token:
        raise exception

    user_id, sig = session_token.split(".", 1)

    if not signature.verify(user_id, sig):
        raise exception

    user = user_service.get_by_id(user_id)

    return UserResponseScheme.model_validate(user)


CurrentUserDep = Annotated[UserResponseScheme, Depends(get_current_user)]
