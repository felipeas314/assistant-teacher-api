from fastapi import FastAPI
from app.core.database import close_mongo_connection
from app.presentation.routers import auth_router, question_router

def create_app() -> FastAPI:
    app = FastAPI()

    @app.on_event("startup")
    async def startup_event():
        print("Aplicação iniciada!")

    @app.on_event("shutdown")
    async def shutdown_event():
        await close_mongo_connection()
    
    app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
    app.include_router(question_router.router, prefix="/questions", tags=["Questions"])
    return app

app = create_app()