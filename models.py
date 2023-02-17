from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(80), primary_key = True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    name = db.Column(db.String(50), nullable = False)
    status = db.Column(db.Boolean, nullable = False)
    status_backref = db.relationship('Category', backref = db.backref('user', lazy = False))

    def __init__(self, login, password, name):
        self.login = login
        self.password = password
        self.name = name
    def __repr__(self):
        return f'{self.id} {self.name}'

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    #user = db.relationship('User', backref = db.backref('feedback', lazy=False))

    text = db.Column(db.Text)

    def __repr__(self):
        return f'{self.id}'

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.Boolean, nullable = False)

class Lunch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appetizer_id = db.Column(db.Integer,db.ForeignKey('appetizer.id'))
    dish_id = db.Column(db.Integer,db.ForeignKey('dish.id'))
    drink_id = db.Column(db.Integer,db.ForeignKey('drink.id'))
    likes_amount = db.Column(db.Integer)
    dislikes_amount = db.Column(db.Integer)

    appetizer = db.relationship('Appetizer', backref = db.backref('lunch', lazy = False))
    dish = db.relationship('Dish', backref=db.backref('lunch', lazy=False))
    drink = db.relationship('Drink', backref=db.backref('lunch', lazy=False))

class Appetizer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    photo = db.Column(db.String)

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    photo = db.Column(db.String(80))
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    photo = db.Column(db.String)




