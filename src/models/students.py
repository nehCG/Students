from src import db


class Student(db.Model):
    db.__tablename__ = 'student'

    uni = db.Column(db.String(10), primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    nationality = db.Column(db.String(64), nullable=False)
    ethnicity = db.Column(db.String(32), nullable=True)
    gender = db.Column(db.String(32), nullable=True)
    admission_date = db.Column(db.String(64), nullable=False)
