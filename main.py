from typing import Optional

from fastapi import FastAPI, Form, Depends, Request
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from crud import *
from db import SessionLocal, engine

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

models.Base.metadata.create_all(bind=engine)

STUDENTS = [
    {
        'id': 1,
        'name': 'Filip',
        'student_class': '1aT'
    },
    {
        'id': 2,
        'name': 'Tymon',
        'student_class': '1aT'
    },
    {
        'id': 3,
        'name': 'Zachary',
        'student_class': '1cT'
    },
]


@app.get("/root", name='Root endpoint', description='My root endpoint')
def root():
    return {"message": "Hello World"}
    # return "Hello World"


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/students", name='Students list')
def get_all_students(request: Request, db: Session = Depends(get_db), ):
    print('HERE', get_students(db))
    students = get_students(db)
    return templates.TemplateResponse('list.html', {'request': request, 'students': students})


@app.get("/student/search", name='Student by name')
def get_student_by_name(name: str, student_class: str = ''):
    for student in STUDENTS:
        if student_class:
            if student['name'] == name and student['student_class'] == student_class:
                return student
        else:
            if student['name'] == name:
                return student


@app.get("/student", name='Student by id')
def get_student_by_id(id: int, db: Session = Depends(get_db)):
    return get_db_student_by_id(db, id)

    # OLD VERSION - WITHOUT DB
    # for student in STUDENTS:
    #     if id == student['id']:
    #         return student


@app.delete('/delete-student', name='Delete student by id')
def delete_student(id: int):
    for student in STUDENTS:
        if student['id'] == id:
            STUDENTS.remove(student)
    return STUDENTS


@app.get('/create-student', name='Create student')
def create_student(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse('create.html', {'request': request})


@app.post('/create-student', name='Create student')
# def create_student(request: Request, student: Student, db: Session = Depends(get_db)):
def create_student(request: Request, name: str = Form(...), surname: str = Form(...), student_class: str = Form(...),
                   db: Session = Depends(get_db)):
    print(name)
    student = Student(name=name, surname=surname, student_class=student_class)
    new_student = create_db_student(db, student)
    # print(s)
    return templates.TemplateResponse('create.html', {'request': request, 'new_student': new_student})

    # STUDENTS.append(student)
    # return {
    #     'message': 'Dodano nowego studenta',
    #     'student': student
    # }


@app.patch('/update-student/', name='Update student')
def update_student(id: int, student: Student):
    old_student = list(filter(lambda x: x['id'] == id, STUDENTS))[0]
    old_student_index = STUDENTS.index(old_student)

    # wersja 1 - zaktualizuje wartosci pól Optional
    STUDENTS[old_student_index] = student

    # wersja 2 - zaktualizuje tylko pola podane, usuwajac pozostale
    # STUDENTS[old_student_index] = student.dict(exclude_unset=True)
    #
    # # wersja poprawna
    # old_student_model = Student(**old_student)
    # update_data = student.dict(exclude_unset=True)
    # updated_student = old_student_model.copy(update=update_data)
    #
    # STUDENTS[old_student_index] = jsonable_encoder(updated_student)
    return STUDENTS

# @app.post('/create-student', name='Create student')
# def create_student(name: str = Form(...), student_class: str = Form(...)):
#     STUDENTS.append({
#         'name': name,
#         'student_class': student_class
#     })
#     return {
#         'message': 'Dodano nowego studenta',
#         # 'student': student
#     }
