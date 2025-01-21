from fastapi import APIRouter

router = APIRouter()

from app.core.database import database
@router.get("/health")
async def health_check():
    print(database)
    if database:
        return {"status":"Database connected"}
    return {"status":"Database not connected"}