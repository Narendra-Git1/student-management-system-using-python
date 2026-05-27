from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.student_schema import (
    StudentCreate,
    StudentResponse
)

from app.models.student import Student
from app.database import get_db

router = APIRouter()


# GET ALL STUDENTS
@router.get(
    "/students",
    response_model=List[StudentResponse]
)
def get_students(db: Session = Depends(get_db)):

    students = db.query(Student).all()

    return students


# GET STUDENT BY ID
@router.get(
    "/students/{id}",
    response_model=StudentResponse
)
def get_student(
    id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(Student.id == id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return student


# ADD STUDENT
@router.post(
    "/students",
    response_model=StudentResponse
)
def add_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    new_student = Student(
        name=student.name,
        email=student.email,
        course=student.course,
        city=student.city
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# UPDATE STUDENT
@router.put(
    "/students/{id}",
    response_model=StudentResponse
)
def update_student(
    id: int,
    updated_student: StudentCreate,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(Student.id == id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    student.name = updated_student.name
    student.email = updated_student.email
    student.course = updated_student.course
    student.city = updated_student.city

    db.commit()
    db.refresh(student)

    return student


# DELETE STUDENT
@router.delete("/students/{id}")
def delete_student(
    id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(Student.id == id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student Deleted Successfully"
    }