from pydantic import BaseModel


# Request Schema
class StudentCreate(BaseModel):
    name: str
    email: str
    course: str
    city: str


# Response Schema
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    course: str
    city: str

    class Config:
        from_attributes = True