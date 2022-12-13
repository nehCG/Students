import unittest
import requests


class TestAddStudent(unittest.TestCase):

    def test_successful_add(self):
        # Given
        student_added = {
            "uni": "ab1234",
            "first_name": "David",
            "last_name": "Martin",
            "nationality": "United States",
            "race": "White",
            "gender": "Male",
            "admission_date": "12/14/2022"
        }

        # When
        response = requests.post('http://localhost:5013/api/students/new_student',
                                 json=student_added)
        # Then
        print(response)
        self.assertEqual(200, response.status_code)
