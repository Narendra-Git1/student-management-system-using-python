from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.auth.auth_handler import hash_password

from app.models.student import Student
from app.schemas.student_schema import StudentCreate


# GET ALL STUDENTS
def get_all_students(db: Session):

    students = db.query(Student).all()

    return students


# GET STUDENT BY ID
def get_student_by_id(id: int, db: Session):

    student = db.query(Student).filter(Student.id == id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return student


# ADD STUDENT
def create_student(student: StudentCreate, db: Session):

    new_student = Student(
        name=student.name,
        email=student.email,
        course=student.course,
        city=student.city,
        password=hash_password(student.password)
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# UPDATE STUDENT
def update_student_service(
    id: int,
    updated_student: StudentCreate,
    db: Session
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
    student.password = hash_password(
        updated_student.password
    )

    db.commit()
    db.refresh(student)

    return student


# DELETE STUDENT
def delete_student_service(id: int, db: Session):

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