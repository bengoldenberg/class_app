import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
app = FastAPI()

class Students(BaseModel):
    firstname: str
    lastname: str
    id: int
    mission: list[str] = []
students_list = []
@app.post("/class/students")
def create_student(student: Students):
    students_list.append(student)
    return students_list

@app.put("/class/students/<int:id>")
def change_student_id(id, new_id):
    for i, stud in students_list:
        find = 'No'
        if stud['id'] == id:
            students_list[i]['id'] = new_id

            find = 'Yes'
    if find == 'No':
        return jsonable_encoder({"error": "not found id"}), 404
    return




@app.get("/class/students")
def get_students(student: Students):
    return student

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)
