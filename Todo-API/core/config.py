from typing import List

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = "Jeevan"
    JWT_REFRESH_SECRET_KEY: str = "Sai Jeevan"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]
    PROJECT_NAME: str = "TodoApp"

    # Database
    MONGO_CONNECTION_STRING: str = "mongodb://localhost:27017"

    class Config:
        case_sensitive = True


settings = Settings()
