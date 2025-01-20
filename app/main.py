# app/main.py

from fastapi import FastAPI
from app.presentation.routers import auth_router
from app.core.config import settings
from app.core.database import connect_to_mongo, close_mongo_connection

def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)

    # Eventos de inicialização e finalização da app
    @app.on_event("startup")
    async def startup_db_client():
        await connect_to_mongo()

    @app.on_event("shutdown")
    async def shutdown_db_client():
        await close_mongo_connection()

    # Inclui as rotas
    app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])

    return app

app = create_app()
