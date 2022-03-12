from typing import Optional
from uuid import uuid4

from pydantic import BaseModel


class Student(BaseModel):
    name: str
    surname: str
    student_class: str

    class Config:
        orm_mode = True
