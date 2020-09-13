from app import db


class Vacancy(db.Model):
    __table_name__ = 'vacancies'
    id = db.Column(db.Integer, primary_key=True)
    # id,name,salary_from,salary_to,currency,area,skill_set,description
    name = db.Column(db.String(64))
    salary_from = db.Column(db.Integer)
    salary_to = db.Column(db.Integer)
    currency = db.Column(db.String(16))
    area = db.Column(db.String(64))
    skill_set = db.Column(db.String(128))
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Vacancy {}>'.format(self.name)
