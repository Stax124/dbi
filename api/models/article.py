from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from sqlmodel import ARRAY, Column, Field, SQLModel, String


class Article(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(min_length=3, max_length=32, index=True)
    content: str = Field(min_length=8, max_length=128)
    author_id: UUID = Field(foreign_key="user.id")
    published: bool = Field(default=False)
    created_date: datetime = Field(default_factory=datetime.now)
    updated_date: datetime = Field(default_factory=datetime.now)
    tags: List[float] = Field(sa_column=Column(ARRAY(String)))
