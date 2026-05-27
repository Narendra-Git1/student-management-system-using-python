from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.schemas.student_schema import StudentCreate
from app.models.student import Student
from app.database import SessionLocal

router = APIRouter()

db = SessionLocal()


# GET ALL STUDENTS
@router.get("/students")
def get_students():

    students = db.query(Student).all()

    return students


# GET STUDENT BY ID
@router.get("/students/{id}")
def get_student(id: int):

    student = db.query(Student).filter(Student.id == id).first()

    if student is None:
        return {"message": "Student Not Found"}

    return student


# ADD STUDENT
@router.post("/students")
def add_student(student: StudentCreate):

    new_student = Student(
        name=student.name,
        email=student.email,
        course=student.course,
        city=student.city
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student Added Successfully",
        "student": new_student
    }


# UPDATE STUDENT
@router.put("/students/{id}")
def update_student(id: int, updated_student: StudentCreate):

    student = db.query(Student).filter(Student.id == id).first()

    if student is None:
        return {"message": "Student Not Found"}

    student.name = updated_student.name
    student.email = updated_student.email
    student.course = updated_student.course
    student.city = updated_student.city

    db.commit()
    db.refresh(student)

    return {
        "message": "Student Updated Successfully",
        "student": student
    }


# DELETE STUDENT
@router.delete("/students/{id}")
def delete_student(id: int):

    student = db.query(Student).filter(Student.id == id).first()

    if student is None:
        return {"message": "Student Not Found"}

    db.delete(student)
    db.commit()

    return {"message": "Student Deleted Successfully"}