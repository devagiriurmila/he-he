from flask import Flask, request, jsonify

app = Flask(__name__)

students = []
id = 1

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    global id
    data = request.get_json()
    
    student = {
        "id": id,
        "name": data["name"],
        "roll": data["roll"]
    }
    
    students.append(student)
    id += 1
    
    return jsonify(student)

@app.route('/students/<int:sid>', methods=['DELETE'])
def delete_student(sid):
    global students
    students = [s for s in students if s["id"] != sid]
    return jsonify({"msg": "Deleted"})

app.run(debug=True,host="0.0.0.0",port=5000)
