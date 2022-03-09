from typing import Optional

from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    surname: str
    student_class: str

    class Config:
        orm_mode = True
