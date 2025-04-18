from datetime import datetime, date
import uuid
from src.reviews.schemas import ReviewModel

from pydantic import BaseModel


class TagModel(BaseModel):
    uid: uuid.UUID
    name: str
    created_at: datetime


class TagCreateModel(BaseModel):
    name: str


class TagAddModel(BaseModel):
    tags: list[TagCreateModel]
