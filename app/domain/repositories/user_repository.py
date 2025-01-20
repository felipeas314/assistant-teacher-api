from typing import Optional
from abc import ABC, abstractmethod
from app.domain.models.user_model import User

class IUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[User]:
        pass