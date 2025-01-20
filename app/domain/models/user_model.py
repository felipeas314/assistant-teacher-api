from typing import Optional
from dataclasses import dataclass

@dataclass
class User:
    id: Optional[str]
    email: str
    hashed_password: str