import unittest
import requests

# clear the database before doing this test


class TestGetStudents(unittest.TestCase):

    def test_empty_response(self):
        response = requests.get('http://localhost:5013/api/students/ab1230')
        self.assertEqual(response.text, 'null\n')
        self.assertEqual(response.status_code, 200)

    def test_student_response(self):
        # Given

        student_added = {
            "uni": "ab1230",
            "first_name": "David",
            "last_name": "Martin",
            "nationality": "United States",
            "race": "White",
            "gender": "Male",
            "admission_date": "12/14/2022"
        }
        response1 = requests.post('http://localhost:5013/api/students/new_student',
                                  json=student_added)

        # When
        response = requests.get('http://localhost:5013/api/students/ab1230')

        # Then
        print(response.text)
        self.assertEqual(200, response.status_code)
