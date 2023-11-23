from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    username: str = Field(min_length=3, max_length=32, index=True)
    password: str = Field(min_length=8, max_length=128)
    avatar: Optional[str] = Field(default=None)
    email: str = Field(max_length=128, index=True)


@dataclass
class UserSafe:
    id: UUID
    username: str
    avatar: Optional[str] = None
