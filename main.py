from typing import Optional

from fastapi import FastAPI, Form
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


class Student(BaseModel):
    id: int
    name: str
    student_class: str


@app.post('/create-student', name='Create student')
def create_student(student: Student):
    STUDENTS.append({
        'id': student.id,
        'name': student.name,
        'student_class': student.student_class,
    })
    return {
        'message': 'Dodano nowego studenta',
        'student': student
    }

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
