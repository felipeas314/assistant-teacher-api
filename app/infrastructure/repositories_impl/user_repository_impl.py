from typing import Optional
from app.domain.models.user_model import User
from app.domain.repositories.user_repository import IUserRepository

class UserRepositoryMongo(IUserRepository):
    COLLECTION = "users"

    def __init__(self, database):
        self.database = database

    async def create_user(self, user: User) -> User:
        user_doc = {"email": user.email, "hashed_password": user.hashed_password}
        result = await self.database[self.COLLECTION].insert_one(user_doc)
        user.id = str(result.inserted_id)
        return user

    async def get_by_email(self, email: str) -> Optional[User]:
        user_doc = await self.database[self.COLLECTION].find_one({"email": email})
        if user_doc:
            return User(
                id=str(user_doc["_id"]),
                email=user_doc["email"],
                hashed_password=user_doc["hashed_password"]
            )
        return None