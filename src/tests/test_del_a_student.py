import unittest
import requests


class TestDelStudent(unittest.TestCase):

    def test_successful_Del(self):
        # Given
        student_del = {
            "uni": "ab1234"
        }

        # When
        response = requests.post('http://localhost:5013/api/students/del_student',
                                 json=student_del)
        # Then
        print(response)
        self.assertEqual(302, response.status_code)
