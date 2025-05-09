from datetime import datetime, date
import uuid
from src.reviews.schemas import ReviewModel
from src.tags.schemas import TagModel

from pydantic import BaseModel


class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime


class BookDetailModel(Book):
    reviews: list[ReviewModel]
    tags: list[TagModel]


class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
