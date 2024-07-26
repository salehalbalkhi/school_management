from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow all origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id: int
    name: str
    grade: int

Students = [
    Student(id=1, name="Alice", grade=100),
    Student(id=2, name="Bob", grade=90),
    Student(id=3, name="Charlie", grade=80),
    Student(id=4, name="David", grade=70)
]

@app.get("/students")
async def read_students():
    return Students

@app.get("/students/{student_id}")
async def read_student(student_id: int):
    for student in Students:
        if student.id == student_id:
            return student
    return {"message": "Student not found"}

@app.post("/students")
async def create_student(student: Student):
    Students.append(student)
    return student

@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    for i in range(len(Students)):
        if Students[i].id == student_id:
            Students[i] = student
            return student
    return {"message": "Student not found"}

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for i in range(len(Students)):
        if Students[i].id == student_id:
            student = Students[i]
            del Students[i]
            return student
    return {"message": "Student not found"}