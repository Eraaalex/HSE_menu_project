from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
db = SQLAlchemy()
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    login = db.Column(db.String(80), nullable = False)
    password = db.Column(db.String(50), nullable = False)
    name = db.Column(db.String(50), nullable = False)
    status = db.Column(db.Boolean, nullable = False)


    def __repr__(self):
        return f'{self.id} {self.name}'

# class Feedback(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
#     users = db.relationship('Users', backref = db.backref('feedback', lazy=False))
#     text = db.Column(db.String)
#
# #     def __repr__(self):
# #         return f'{self.id}'


class Lunch(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    appetizer_id = db.Column(db.Integer,db.ForeignKey('appetizer.id'))
    dish_id = db.Column(db.Integer,db.ForeignKey('dish.id'))
    drink_id = db.Column(db.Integer,db.ForeignKey('drink.id'))
    likes_amount = db.Column(db.Integer)
    dislikes_amount = db.Column(db.Integer)

    appetizer = db.relationship('Appetizer', backref = db.backref('lunch', lazy = False))
    dish = db.relationship('Dish', backref=db.backref('lunch', lazy=False))
    drink = db.relationship('Drink', backref=db.backref('lunch', lazy=False))
    def get_appetizer_name(self):
        return db.session().query(Appetizer).filter_by(id = self.appetizer_id).first().name
    def get_dish_name(self):
        return db.session().query(Dish).filter_by(id = self.appetizer_id).first().name
    def get_drink_name(self):
        return db.session().query(Drink).filter_by(id = self.appetizer_id).first().name

class Appetizer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    photo = db.Column(db.String)

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    photo = db.Column(db.String(80))
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    photo = db.Column(db.String)
# class Account (db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     login = db.Column(db.String(80), primary_key=True, nullable=False)
#     password = db.Column(db.String(50), nullable=False)
#     name = db.Column(db.String(50), nullable=False)
#     status = db.Column(db.Boolean, nullable=False)



