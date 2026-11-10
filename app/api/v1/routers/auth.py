from fastapi import APIRouter, Response, HTTPException, status
from app.core.schemes.user import UserRequestScheme, UserResponseScheme
from app.core.security.auth import authentication
from app.core.security.signature import signature
from app.api.dependencies.database import UserServiceDep

router = APIRouter(tags=["Auth"])


@router.post(
    "/register",
    response_model=UserResponseScheme,
    status_code=status.HTTP_201_CREATED
)
def register_endpoint(
    user: UserRequestScheme,
    user_service: UserServiceDep
):
    existing_user = user_service.get_by_username(user.username) or user_service.get_by_email(user.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь уже с таким username или email существует"
        )

    user_response = user_service.add(user)
    return user_response


@router.post("/login")
def login_endpoint(
    user: UserRequestScheme,
    response: Response,
    user_service: UserServiceDep
) -> dict[str, str]:
    existing_user = authentication(user_service, user.username, user.password.get_secret_value())

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользватель не авторизован в системе"
        )

    response.set_cookie(
        key="session_token",
        value=f"{existing_user.id}.{signature.generate(existing_user.id)}",
        max_age=3600,
        httponly=True
    )

    return {
        "message": "Добро пожаловать!"
    }


@router.post("/logout")
def logout_handler(response: Response) -> dict[str, str]:
    response.delete_cookie(key="session_token")
    return {
        "message": "Еще увидимся!"
    }
