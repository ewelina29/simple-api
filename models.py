# from sqlalchemy import String, Column
from sqlalchemy import Column, String, Integer

from db import Base


class StudentModel(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    student_class = Column(String)
