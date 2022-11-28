import unittest
import requests


class TestDelStudent(unittest.TestCase):

    def test_successful_Del(self):
        # Given
        student_update = {
            "uni": "ab1234",
            "first_name": "Daviiiid",
            "last_name": "Martin",
            "nationality": "United States",
            "ethnicity": "White",
            "gender": "Male",
            "admission_date": "12/14/2022"
        }

        # When
        response = requests.post('http://localhost:5013/api/students/update_student',
                                 json=student_update)
        # Then
        print(response)
        self.assertEqual(200, response.status_code)
