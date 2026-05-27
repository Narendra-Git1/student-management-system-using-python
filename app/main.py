from fastapi import FastAPI
from app.routers import student_router
from app.database import engine, Base
from app.models.student import Student

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student_router.router)

@app.get("/")
def home():
    return {"message": "Student Management System Backend Running"}