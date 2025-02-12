from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from database import db, Announcement, Event, Birthday

app = Flask(__name__)
CORS (app)# Allows Power Bi to fetch data

#Configuring SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///office_dashboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app (app)

#API Endpoint

@app.route('/updates', methods=['GET'])
def get_updates():
    announcements = Announcement.query_class.order_by (Announcement.date_posted.desc()).all()
    events = Event.query.order_by (Event.date.asc()).all()
    birthdays = Birthday.query.all()

    return jsonify ({
        "announcemets":  [{"title": a.title, "content": a.content, "date": a.date_posted} for a in announcements],
        "events": [{"name": e.name, "date": e.date, "description": e.description} for e in events],
        "birthdays": [{"name": b.employee_name, "date": b.birthdate} for b in birthdays]
    })

@app.route ('/event', methods=['POST'])
def add_event():
    data = request.json
    new_event = Event(name=data['name'], date=datetime.strptime(data['date'], "%Y-%m-%d"), description=data['description'])
    db.session.add(new_event)
    db.session.commit()
    return jsonify ({"message": "Event added successfully!"}), 201

@app.route('/birthday', methods = ['POST'])
def add_birthday():
    data = request.json
    new_birthday = Birthday (employee_name=data['name'], birthdate=datetime.strptime(data['birthdate'], "%Y-%m-%d"))
    db.session.add (new_birthday)
    db.session.commit()
    return jsonify ({"message": "Birthday added successfully!"}), 201

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Office Dashboard API!", 200

#Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all() #Create tables
    app.run (debug = True)