from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

STUDENTS = [
    {
        'name': 'Filip',
        'student_class': '1aT'
    },
    {
        'name': 'Tymon',
        'student_class': '1aT'
    },
    {
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


class Student(BaseModel):
    name: str
    student_class: str


@app.post('/create-student', name='Create student')
def create_student(student: Student):
    STUDENTS.append({
        'name': student.name,
        'student_class': student.student_class
    })
    return {
        'message': 'Dodano nowego studenta',
        'student': student
    }
