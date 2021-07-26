import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Students(BaseModel):
    firstname: str
    lastname: str
    id: int
    mission: list[str] = []

@app.post("/class/students")
def create_student(student: Students):
    return student

@app.put("/class/students")
def create_student(student: Students):
    return student


@app.get("/class/students")
def get_students(student: Students):
    return student

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)
