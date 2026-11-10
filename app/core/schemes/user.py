from datetime import datetime, timezone
from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field, SecretStr, field_validator

from app.core.utils.password import validate_password

__all__ = ("UserRequestScheme", "UserResponseScheme",)


class UserBaseScheme(BaseModel):
    username: Annotated[str, Field(examples=["Alex"], min_length=3, max_length=50)]
    email: EmailStr
    password: Annotated[SecretStr, Field(examples=["qwerty123!ABC"], min_length=8, max_length=20)]

    @field_validator("username")
    @classmethod
    def _validate_username(cls, username: str) -> str:
        if not username.isalpha():
            raise ValueError("Имя пользователя должно содержать только буквы")

        return username

    @field_validator("password")
    @classmethod
    def _validate_password(cls, password: SecretStr) -> SecretStr:
        value = password.get_secret_value()

        validate_password(value)

        return password


class UserRequestScheme(UserBaseScheme):
    ...


class UserResponseScheme(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: str
    username: str
    email: str
    password: Annotated[SecretStr, Field(exclude=True)]
    created_at: datetime
