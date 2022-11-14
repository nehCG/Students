from flask import request, jsonify

from src import app

from src.resources.student_resource import StudentResource


@app.route('/api/students/new_student', methods=['POST'])
def add_new_student():
    data = request.json
    if StudentResource.get_student_uni(data['first_name'],
                                       data['last_name'],
                                       data['nationality'],
                                       data['ethnicity'],
                                       data['gender'],
                                       data['admission_date']) is not None:
        response = jsonify('Student already exists!')
        response.status_code = 400
        return response

    StudentResource.add_new_student(data['uni'],
                                    data['first_name'],
                                    data['last_name'],
                                    data['nationality'],
                                    data['ethnicity'],
                                    data['gender'],
                                    data['admission_date'])

    response = jsonify('Successfully added')
    response.status_code = 200
    return response


@app.route('/api/students/uni', methods=['GET'])
def get_one_student(uni):
    student = StudentResource.search_student_by_uni(uni)

    response = jsonify(student)
    response.status_code = 200
    return response


@app.route('/api/students', methods=['GET'])
def get_all_students():
    students = StudentResource.search_all_students()

    response = jsonify(students)
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5011)
