import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


student_list = []

class Student(BaseModel):
    firstname: str
    lastname: str
    id: int
    mission: list

@app.post("/class/students")
def create_student(student: Student):
    student_list.append(student)
    return student_list

@app.put("/class/students")
def create_student(new_student: Student):
    for index, student in enumerate(student_list):
        if student.id == new_student.id:
            student_list[index] = new_student
    return student_list

@app.get("/class/students")
def get_students():
    return student_list

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)
