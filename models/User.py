from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    senderId: int
    nickname: str
    username: Optional[str] = None
