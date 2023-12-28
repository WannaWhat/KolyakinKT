from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class StudentModel(BaseModel):
    id: Optional[UUID] = None
    age: int
    name: str
    surname: str
    group: str
    course: int