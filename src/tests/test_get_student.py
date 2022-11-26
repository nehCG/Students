import json

from .BaseCase import BaseCase


class TestGetStudents(BaseCase):

    def test_empty_response(self):
        response = self.app.get('/api/students/uni')
        self.assertListEqual(response.json, [])
        self.assertEqual(response.status_code, 200)

    def test_student_response(self):
        # Given
        student_added = {
            "uni": "ab1234",
            "first_name": "David",
            "last_name": "Martin",
            "nationality": "United States",
            "ethnicity": "White",
            "gender": "Male",
            "admission_date": "12/14/2022"
        }

        response = self.app.post('/api/students/uni',
                                 headers={"Content-Type": "application/json"},
                                 data=json.dumps(student_added))

        # When
        response = self.app.get('/api/students/uni')
        added_student = response.json[0]

        # Then
        self.assertEqual(student_added['first_name'], added_student['first_name'])
        self.assertEqual(student_added['last_name'], added_student['last_name'])
        self.assertEqual(student_added['nationality'], added_student['nationality'])
        self.assertEqual(student_added['ethnicity'], added_student['ethnicity'])
        self.assertEqual(student_added['gender'], added_student['gender'])
        self.assertEqual(student_added['admission_date'], added_student['admission_date'])
        self.assertEqual(200, response.status_code)
