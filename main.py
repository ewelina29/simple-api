from typing import Optional

from fastapi import FastAPI, Form
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

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


class Student(BaseModel):
    id: Optional[int] = 0
    # id: int
    name: str
    student_class: str


@app.get("/root", name='Root endpoint', description='My root endpoint')
def root():
    return {"message": "Hello World"}
    # return "Hello World"


@app.get("/students", name='Students list')
def get_students():
    return STUDENTS


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
def get_student_by_id(id: int):
    for student in STUDENTS:
        if id == student['id']:
            return student


@app.delete('/delete-student', name='Delete student by id')
def delete_student(id: int):
    for student in STUDENTS:
        if student['id'] == id:
            STUDENTS.remove(student)
    return STUDENTS


# TO-DO metoda modyfikująca dane ucznia
# @app.put()


@app.post('/create-student', name='Create student')
def create_student(student: Student):
    # STUDENTS.append({
    #     'id': student.id,
    #     'name': student.name,
    #     'student_class': student.student_class,
    # })
    STUDENTS.append(student)
    return {
        'message': 'Dodano nowego studenta',
        'student': student
    }


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
