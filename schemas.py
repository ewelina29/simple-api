from typing import Optional

from pydantic import BaseModel


class Student(BaseModel):
    id: Optional[int] = 0
    # id: int
    name: str
    surname: str
    student_class: str

    class Config:
        orm_mode = True
