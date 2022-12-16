from fastapi import APIRouter
from api.api.handlers import user
from api.api.handlers import todo
from api.auth.jwt import auth_router

router = APIRouter()

# All the routes of API version 1 are combined here.
router.include_router(user.user_router, prefix="/users", tags=["users"])
router.include_router(todo.todo_router, prefix="/todo", tags=["todo"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
