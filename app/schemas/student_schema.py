from pydantic import BaseModel


# REQUEST SCHEMA
class StudentCreate(BaseModel):
    name: str
    email: str
    course: str
    city: str
    password: str


# RESPONSE SCHEMA
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    course: str
    city: str

    class Config:
        from_attributes = True