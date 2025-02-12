from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Announcement (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    title = db.Column (db.String(255), nullable = False)
    content = db.Column (db.Text, nullable = False)
    date_posted = db.Column (db.DateTime, default = db.func.current_timestamp())

class Event (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.String(255), nullable = False)
    date = db.Column (db.DateTime, nullable = False)
    description = db.Column (db.text)

class Birthday (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    employee_name = db.Column (db.String(255), nullable = False)
    birthdate = db.Column (db.Date, nullable = False)