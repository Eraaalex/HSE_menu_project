from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from datetime import datetime
db = SQLAlchemy()
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    login = db.Column(db.String(80), nullable = False, unique=True)
    password = db.Column(db.String(50), nullable = False)
    name = db.Column(db.String(50), nullable = False)
    status = db.Column(db.Boolean, nullable = False)

    def __repr__(self):
        return f'{self.id} {self.name}'

    @staticmethod
    def get_user_by_email(email):
        return db.session().query(Users).filter_by(login = email).scalar()
    @staticmethod
    def get_user_by_id(id):
        return db.session().query(Users).filter_by(id = id).scalar()



class Lunch(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
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
        return db.session().query(Dish).filter_by(id = self.dish_id).first().name
    def get_drink_name(self):
        return db.session().query(Drink).filter_by(id = self.drink_id).first().name
    def get_drink_photo(self):
        return db.session().query(Drink).filter_by(id = self.drink_id).first().photo
    def get_appetizer_photo(self):
        return db.session().query(Appetizer).filter_by(id = self.appetizer_id).first().photo
    def get_dish_photo(self):
        return db.session().query(Dish).filter_by(id = self.dish_id).first().photo

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
class Orders(db.Model):
    __tablename__ ='orders'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lunch_id = db.Column(db.Integer, db.ForeignKey('lunch.id'))
    date= db.Column(db.DateTime, nullable=False,default=datetime.utcnow())
    lunch = db.relationship('Lunch', backref=db.backref('orders', lazy=False))
    user = db.relationship('Users', backref=db.backref('orders', lazy=False))
    def get_user_name_by_id(self):
        return db.session().query(Users).filter_by(id = self.user_id).first().name
    def get_lunch_by_id(self):
        return db.session().query(Lunch).filter_by(id = self.lunch_id).first()