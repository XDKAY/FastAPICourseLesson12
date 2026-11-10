from fastapi import APIRouter
from .v1 import routers_v1


__all__ = ("api_routers", )


api_routers = APIRouter(prefix="/api")
api_routers.include_router(routers_v1)
