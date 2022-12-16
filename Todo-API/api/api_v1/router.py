from fastapi import APIRouter
from api.api_v1.handlers import user
from api.api_v1.handlers import todo
from api.auth.jwt import auth_router

router = APIRouter()

router.include_router(user.user_router, prefix='/users', tags=["users"])
router.include_router(todo.todo_router, prefix='/todo', tags=["todo"])
router.include_router(auth_router, prefix='/auth', tags=["auth"])