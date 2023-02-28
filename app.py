from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *
from flask import Flask, render_template, escape, abort, request, flash
from service import *
from basic_input import *
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret'
@app.route('/')
def index():
    day_of_week = datetime.now().weekday()
    lunch = db.session.query(Lunch).filter_by(id = day_of_week + 1).all()
    return render_template("index.html",lunch = lunch[0],
                          activeT = "active", activeW = "", style_name ="index")

@app.route('/week')
def weekPage():
    return render_template("week.html", lunches = db.session.query(Lunch).all(),
                           activeT = "", activeW = "active", style_name = "week")

@app.route('/account', methods=['GET', 'POST'])
def accountPage():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        print(name,login,password)
        if (name !=None and  password!=None and login!=None ):
            user = addUser(login = login, password = password,name = name, status = True)
        elif (password!=None and login!=None):
            user = db.session.query(Users).filter_by(login = login, password = password).scalar()
            if user != None:
                return render_template("userPage.html", user = user) # rewrite
    return render_template("account.html")

@app.route('/account/<name>')
def product(name):
    name=escape(name)
    return render_template('userPage.html', user =db.session.query(Users).filter_by(name=name).one())

# @app.route('/Main', method =['GET', 'POST'])
# def main():
#     if request.method == 'POST':
#         login = request.form.get('login')
#         text = request.form.get('review')
#         if (login!='' and text!='')
#             user = db.session.query(Users).filter(Users.login == login).one()
#             #fd = Feedback(user.id, text)
#             addFeedback(fd)
#     return render_template('...html', feedbacks = db.session.query(Feedback).all() )
#
# @app.route('/Menu', method =['GET', 'POST'])
# def menu():
#     return render_template('Menu.html', items = db.session.query(Lunch).all())

# @app.route('/account/<name>')
# def product(name):
#     name=escape(name)
#     name_list = db.session.query(Users.name).all()
#     for el in products:
#         if el.name==item:
#             return render_template('Product.html',item = el)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:eralex@localhost:5432/project_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
flag = False
if __name__ == '__main__':
    with app.app_context():
        #db.create_all()
        #basic_input()
        print("OK")

    app.run(debug=True)

