from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Car(db.Model):
    toy_num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    series = db.Column(db.String(20), unique=False, nullable=True)
    year = db.Column(db.Integer, unique=False, nullable=False)
    photo_url = db.Column(db.String(80), unique=True, nullable=True)


@app.route("/")
def index():
    return 'Hello!'


@app.route('/cars')
def get_cars():
    cars = {'car': 'car data'}
    return cars
