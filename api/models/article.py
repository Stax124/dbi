from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class Article(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(min_length=3, max_length=32, index=True)
    content: str = Field(min_length=8, max_length=128)
    author_id: UUID = Field(foreign_key="user.id")
