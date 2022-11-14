from src import db
from src.models.students import Student


class StudentResource:
    def __int__(self):
        pass

    @staticmethod
    def add_new_student(uni, first_name, last_name, nationality, ethnicity, gender, admission_date):
        student = Student(uni=uni,
                          first_name=first_name,
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

    @staticmethod
    def search_student_by_uni(student_uni):
        return db.session.query(Student).filter_by(uni=student_uni).first()

    @staticmethod
    def search_all_students():
        return db.session.query(Student).all()


