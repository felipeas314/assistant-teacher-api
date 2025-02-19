from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Clean Arch Example"
    MONGO_URI: str = "mongodb://root:example@localhost:27017"
    MONGO_DB_NAME: str = "fastapi_clean_arch_db"
    JWT_SECRET: str = "SUPER_SECRET_JWT"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    OPENAI_API_KEY: str = "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"

    class Config:
        env_file = ".env"

settings = Settings()
