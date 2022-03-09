from sqlalchemy.orm import Session

import models
import schemas
from schemas import Student


def get_students(db: Session):
    return db.query(models.StudentModel).all()


def create_db_student(db: Session, student: schemas.Student):
    db_student = models.StudentModel(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_db_student_by_id(db: Session, id: int):
    return db.query(models.StudentModel).get(id)
