from typing import Optional
from app.domain.repositories.user_repository import IUserRepository
from app.domain.models.user_model import User
from app.core.security import get_password_hash, verify_password, create_access_token

class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def register_user(self, email: str, password: str) -> User:
        # Verifica se já existe
        existing_user = await self.user_repository.get_by_email(email)
        if existing_user:
            raise ValueError("Email já cadastrado.")
        
        hashed = get_password_hash(password)
        new_user = User(id=None, email=email, hashed_password=hashed)
        created_user = await self.user_repository.create_user(new_user)
        return created_user

    async def authenticate_user(self, email: str, password: str) -> Optional[str]:
        user = await self.user_repository.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        # Se validou, gera token
        token = create_access_token(user.email)
        return token
