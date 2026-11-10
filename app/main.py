from fastapi import FastAPI

from .api import api_routers

app = FastAPI()

app.include_router(api_routers)
