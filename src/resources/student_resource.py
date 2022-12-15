from src import db
from src.models.students import Student


class StudentResource:
    def __int__(self):
        pass

    @staticmethod
    def add_new_student(uni, first_name, last_name, nationality, race, gender, admission_date):
        student = Student(uni=uni,
                          first_name=first_name,
                          last_name=last_name,
                          nationality=nationality,
                          race=race,
                          gender=gender,
                          admission_date=admission_date)
        db.session.add(student)
        db.session.commit()

    @staticmethod
    def del_a_student(uni):
        student = db.session.query(Student).filter_by(uni=uni).first()
        db.session.delete(student)
        db.session.commit()

    @staticmethod
    def update_a_student(uni, first_name, last_name, nationality, race, gender, admission_date):
        student = db.session.query(Student).filter_by(uni=uni).update({
                          'uni': uni,
                          'first_name': first_name,
                          'last_name': last_name,
                          'nationality': nationality,
                          'race': race,
                          'gender': gender,
                          'admission_date': admission_date})
        db.session.commit()

    @staticmethod
    def search_student_by_uni(student_uni):
        res = db.session.query(Student).filter_by(uni=student_uni).first()
        if res is None:
            return None

        student_list = []
        StudentResource.parse_student_info([res], student_list)
        return student_list

    @staticmethod
    def search_all_students():
        students = db.session.query(Student).all()

        student_list = []
        StudentResource.parse_student_info(students, student_list)

        return student_list


    @staticmethod
    def get_all_names():
        students = db.session.query(Student).all()

        student_name_dict = {}
        for student in students:
            student_name_dict[student.uni] = f'{student.first_name} {student.last_name}'
        return student_name_dict

    @staticmethod
    def parse_student_info(students, student_list):
        for student in students:
            student_dict = {'uni': student.uni,
                            'first_name': student.first_name,
                            'last_name': student.last_name,
                            'nationality': student.nationality,
                            'race': student.race,
                            'gender': student.gender,
                            'admission_date': student.admission_date}
            student_list.append(student_dict)
