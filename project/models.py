from project import db
import datetime
from flask import jsonify


class Customer(db.Model):
    """ Customer Model for storing user related details """
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_id = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    second_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)

    def __init__(self, car_id, first_name, second_name, address, phone):
        self.car_id = car_id
        self.first_name = first_name
        self.second_name = second_name
        self.address = address
        self.phone = phone

    def __repr__(self):
        return {'car_id': self.car_id,
                'first_name': self.first_name,
                'second_name': self.second_name,
                'address': self.address,
                'phone': self.phone}

    def as_dict(self):
        return {'car_id': self.car_id,
                'first_name': self.first_name,
                'second_name': self.second_name,
                'address': self.address,
                'phone': self.phone}


class Order(db.Model):
    """
    Orders Model for storing reservations for parking
    """
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime,
                     nullable=False,
                     default=datetime.datetime.now())
    car_id = db.Column(db.String(255),
                       db.ForeignKey('customers.car_id'),
                       nullable=False)
    place_id = db.Column(db.Integer,
                         db.ForeignKey('parking.id'),
                         nullable=False)

    customer = db.relationship('Customer',
                               backref=db.backref('posts', lazy=True))
    parking = db.relationship('Place',
                              backref=db.backref('posts', lazy=True))

    def __init__(self, date, car_id):
        self.date = date
        self.car_id = car_id

    def __repr__(self):
        return jsonify({'date': self.date,
                        'car_id': self.car_id})


class Place(db.Model):
    __tablename__ = 'parking'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
