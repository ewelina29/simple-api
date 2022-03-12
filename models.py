# from sqlalchemy import String, Column
# from uuid import uuid4, UUID
import uuid

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID

from db import Base


class StudentModel(Base):
    __tablename__ = 'student'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    surname = Column(String)
    student_class = Column(String)
