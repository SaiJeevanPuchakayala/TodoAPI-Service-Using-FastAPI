from beanie import init_beanie
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from api.api.router import router
from core.config import settings
from models.todo_model import Todo
from models.user_model import User

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def app_init():
    """
    initializing required startup configurations.
    """

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).TodoApp

    await init_beanie(database=db_client, document_models=[User, Todo])


app.include_router(router, prefix=settings.API_STR)
