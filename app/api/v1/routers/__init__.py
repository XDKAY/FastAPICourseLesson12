from fastapi import APIRouter
from .auth import router as auth_router
from .user import router as user_router


routers = APIRouter()
routers.include_router(auth_router)
routers.include_router(user_router)
