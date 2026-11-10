from fastapi import APIRouter
from .routers import routers


__all__ = ("routers_v1", )


routers_v1 = APIRouter(prefix="/v1")
routers_v1.include_router(routers)
