from fastapi import APIRouter
from app.core.schemes.user import UserResponseScheme
from app.api.dependencies.current_user import CurrentUserDep

router = APIRouter(tags=["User"])


@router.get("/profile", response_model=UserResponseScheme)
def profile_handler(current_user: CurrentUserDep):
    return current_user
