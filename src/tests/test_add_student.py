import json

from src.tests.BaseCase import BaseCase


class TestAddStudent(BaseCase):

    def test_successful_add(self):
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

        # When
        response = self.app.post('/api/students/new_student',
                                 headers={"Content-Type": "application/json"},
                                 data=json.dumps(student_added))
        # Then
        self.assertEqual(200, response.status_code)
