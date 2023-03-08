# run 'python -m unittest test_app.py'
# 'python -m unittest -v test_app.py' to produce more verbose output
# pep8 --first app.py
from sqlalchemy.exc import IntegrityError
from app import app, db
import unittest
import logging
from service import *


class AppTest(unittest.TestCase):
    # web = app.app.test_client()
    # rv = web.get('/')
    # assert rv.status == '200 OK'
    # assert b'<form action="/goto" method="POST">' in rv.data
    def setUp(self):
        with app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()
            assert len(db.session.query(Users).all()) == 0

    def tearDown(self):
        with app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()
            assert len(Users.query.all()) == 0

#
    def test_create_user(self):
        with app.app_context():
            email = 'test_email@email.ru'
            password = 'test_password'
            name = "test-ame"
            user = addUser(login=email, password=password, name = name)
            assert user in db.session
            assert len(Users.query.filter_by(login=email).all()) == 1
            user_from_db = Users.get_user_by_email(email)
            assert user_from_db.login == email
            assert user_from_db.password == (password)

            db.session.commit()

            assert len(Users.query.filter_by(login=email).all()) == 1

    def test_get_user_by_id(self):
        with app.app_context():
            email = 'test_email@email.ru'
            password = 'test_password'
            name = "test-ame"
            user = addUser(login=email, password=password, name = name)

            assert user in db.session

            assert len(Users.query.filter_by(id=1).all()) == 1
            user_from_db = Users.get_user_by_id(1)
            assert user_from_db.login == email

    def test_user_already_exists_raises_integrity_error(self):
        with app.app_context():
            addUser(login='email', password='password', name = 'name')
            l = lambda: (addUser(login='email', password='another', name = 'name'))
            self.assertRaises(IntegrityError, l)
# #
    def test_user_doesnt_exist_returns_none(self):
        with app.app_context():
            user = Users.get_user_by_email("bla")
            assert user is None
            user2 = Users.get_user_by_id(100000)
            assert user2 is None

    def test_user_incorrect_password(self):
        with app.app_context():
            email = 'email'
            password = 'password'
            name = 'test_name'
            addUser(login=email, password='test_password', name = name)
            user = Users.get_user_by_email(email)
            assert user.password != password
if __name__ == '__main__':
    unittest.main()