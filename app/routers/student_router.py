from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.student_schema import (
    StudentCreate,
    StudentResponse
)

from app.database import get_db

from app.services.student_service import (
    get_all_students,
    get_student_by_id,
    create_student,
    update_student_service,
    delete_student_service
)

router = APIRouter()


# GET ALL STUDENTS
@router.get(
    "/students",
    response_model=List[StudentResponse]
)
def get_students(db: Session = Depends(get_db)):

    return get_all_students(db)


# GET STUDENT BY ID
@router.get(
    "/students/{id}",
    response_model=StudentResponse
)
def get_student(
    id: int,
    db: Session = Depends(get_db)
):

    return get_student_by_id(id, db)


# ADD STUDENT
@router.post(
    "/students",
    response_model=StudentResponse
)
def add_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    return create_student(student, db)


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

    return update_student_service(
        id,
        updated_student,
        db
    )


# DELETE STUDENT
@router.delete("/students/{id}")
def delete_student(
    id: int,
    db: Session = Depends(get_db)
):

    return delete_student_service(id, db)