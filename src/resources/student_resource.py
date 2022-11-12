from src import db
from src.models.students import Student


class StudentResource:
    def __int__(self):
        pass

    @staticmethod
    def add_new_student(first_name, last_name, nationality, ethnicity, gender, admission_date):
        student = Student(first_name=first_name,
                          last_name=last_name,
                          nationality=nationality,
                          ethnicity=ethnicity,
                          gender=gender,
                          admission_date=admission_date)
        db.session.add(student)
        db.session.commit()

    @staticmethod
    def get_student_uni(first_name, last_name, nationality, ethnicity, gender, admission_date):
        return db.session.query(Student.uni).filter_by(first_name=first_name,
                                                       last_name=last_name,
                                                       nationality=nationality,
                                                       ethnicity=ethnicity,
                                                       gender=gender,
                                                       admission_date=admission_date).first()
