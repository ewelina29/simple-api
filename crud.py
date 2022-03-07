from sqlalchemy.orm import Session

import models
from schemas import Student


def get_students(db: Session):
    return db.query(models.StudentModel).all()
