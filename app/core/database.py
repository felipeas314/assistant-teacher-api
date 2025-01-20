from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

mongo_client: AsyncIOMotorClient = None
database = None

async def connect_to_mongo():
    global mongo_client, database
    mongo_client = AsyncIOMotorClient(settings.MONGO_URI)
    database = mongo_client[settings.MONGO_DB_NAME]
    print("Conectado ao MongoDB!")

async def close_mongo_connection():
    global mongo_client
    mongo_client.close()
    print("Conexão com MongoDB fechada.")
