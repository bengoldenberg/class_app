from flask import Flask, jsonify, request
import requests
app = Flask(__name__)

Students=[
    {
        "firstname": 'Lebron' ,
        "lastname": 'James' ,
        "id" : 1 ,
        "class" : 'D3'
    }
]
#get all students
@app.route("/school/students", methods=['GET'])
def get_students():
    return jsonify(Students)

#get all students from class
@app.route("/school/<classes>", methods=['GET'])
def get_all_students_from_class(classes):
    stud_list = []
    for student in Students:
        if student['class'] == str(classes):
            stud_list.append(student)
    if len(stud_list) == 0:
        return jsonify({"error": f"the class {classes} is not exists"})
    return jsonify(stud_list)

#create a new student
@app.route("/school/students", methods=['POST'])
def create_new_students():
    content = request.json
    Students.append(content)
    return jsonify(Students)
#change student class
@app.route("/school/class/<int:id>/<classes>", methods=['PUT'])
def chnage_student_class(id,classes):
    i = 0
    for student in Students:
        find = 'No'
        if student['id'] == id:
            Students[i]['class'] = classes
            find = 'Yes'

        i += 1
    if find == 'No':
        return jsonify({"error": "the student isn't exists"})
    return f"the student {id} was moved to class {classes}"
    return jsonify(Students)

#update id of student
@app.route("/school/students/<int:id>/<int:new_id>", methods=['PUT'])
def update_id(id, new_id):
    i = 0
    for student in Students:
        find = 'No'
        if student['id'] == id:
           Students[i]['id'] = new_id
           find = 'Yes'
           firstname = Students[i]['firstname']
           lastname = Students[i]['lastname']
        i += 1
    if find == 'No':
        return jsonify({"error": "the student isn't exists"})
    return f"the student {firstname}  {lastname} id is changed to {new_id}"
    return jsonify(Students)
#delete a user by id
@app.route("/school/students/<int:id>", methods=['DELETE'])
def delete_student(id):
    i = 0
    find = 'No'
    for student in Students:
        if student['id'] == id:
            Students.remove(student)
            find = 'Yes'
            firstname = Students[i]['firstname']
            lastname = Students[i]['lastname']
    if find == 'No':
        return jsonify({"error":"student not found"})
    return jsonify(Students)
    return jsonify(f"the student {firstname} {lastname} with id {id} was deleted")

if __name__ == '__main__':
    app.run( port=80, host="0.0.0.0")
