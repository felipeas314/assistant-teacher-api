from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

mongo_client: AsyncIOMotorClient = None

async def get_database():
    """
    Retorna a instância do banco de dados.
    """
    global mongo_client
    if not mongo_client:
        mongo_client = AsyncIOMotorClient(settings.MONGO_URI)
        print("Conexão com MongoDB estabelecida!")
    return mongo_client[settings.MONGO_DB_NAME]

async def close_mongo_connection():
    """
    Fecha a conexão com o MongoDB.
    """
    global mongo_client
    if mongo_client:
        mongo_client.close()
        print("Conexão com MongoDB encerrada.")