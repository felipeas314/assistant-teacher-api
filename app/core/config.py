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
