from flask import request, jsonify

from src import app

from src.resources.student_resource import StudentResource


@app.route('/api/students/new_student', methods=['POST'])
def add_new_student():
    """JSON copy to test on Postman
    {
        "uni": ab1234
        "first_name": David
        "last_name": Martin
        "nationality": United States
        "ethnicity": White
        "gender": Male
        "admission_date": 12/14/2022
    }
    """
    data = request.json

    if StudentResource.search_student_by_uni(data['uni']) is None:
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
    """JSON copy to test on Postman
    {
        "uni": ab1234
        "first_name": David
        "last_name": Martin
        "nationality": United States
        "ethnicity": White
        "gender": Male
        "admission_date": 12/14/2022
    }
    """
    student = StudentResource.search_student_by_uni(uni)

    response = jsonify(student)
    response.status_code = 200
    return response


@app.route('/api/students', methods=['GET'])
def get_all_students():
    """JSON copy to test on Postman
    {
        {
            "uni": ab1234
            "first_name": David
            "last_name": Martin
            "nationality": United States
            "ethnicity": White
            "gender": Male
            "admission_date": 12/14/2022
        },
        {
            (second student)
        }
    }
    """
    students = StudentResource.search_all_students()

    response = jsonify(students)
    response.status_code = 200
    return response


if __name__ == '__main__':
    # this microservice runs on port number 5013
    app.run(host="0.0.0.0", port=5013)
