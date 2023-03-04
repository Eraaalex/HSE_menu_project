from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask import Flask,redirect, url_for, render_template, escape, abort, request, flash
from service import *
from basic_input import *
from datetime import datetime


DBUSER = 'postgres'
DBPASS = 'eralex'
DBHOST = 'localhost'
DBPORT = '5432'
DBNAME = 'project_db'

app = Flask(__name__)
app.secret_key = 'secret'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:eralex@localhost:5432/project_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = u'Please log in to access this page.'
login_manager.login_message_category = 'error'
migrate = Migrate(app, db)
@app.route('/')
def index():
    day_of_week = datetime.now().weekday()
    lunch = db.session.query(Lunch).filter_by(id = day_of_week + 1).scalar()
    if (lunch is None):
        return render_template('eror404.html')

    print("!!!!!!")
    addit = "/cart" if (current_user is None) else "/cart_empty"
    return render_template("index.html",lunch = lunch,
                          activeT = "active", activeW = "", addition = addit)

@app.route('/week')
@login_required
def weekPage():
    return render_template("week.html", lunches = db.session.query(Lunch).all(),
                           activeT = "", activeW = "active", style_name = "week")

@app.route('/cart_empty')
def cart_empty():
    return render_template("cart_empty.html", lunches = db.session.query(Lunch).all(),
                           activeT = "active", activeW = "active", style_name = "week")

@app.route('/account', methods=['GET', 'POST'])
def registerPage():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')

        if (name !=None and password!=None and login!=None ):
            user = addUser(login = login, password = password,name = name, status = True)
            login_user(user, remember=True)
            return redirect(url_for('accountPage', name = user.name), code =301)
        elif (password!=None and login!=None):
            user = db.session.query(Users).filter_by(login = login, password = password).first()
            if user != None:
                login_user(user, remember=True)
                return redirect(url_for('accountPage', name = user.name),  code=301)
        flash('Wrong login or password', 'danger')
    return render_template("account.html")

@app.route('/account/<name>')
@login_required
def accountPage(name):
    name=escape(name)
    user = db.session.query(Users).filter_by(name=name).first()
    if (user is None):
        return render_template("error404.html")
    return render_template('userPage.html', user = user)

@login_manager.user_loader
def load_user(userid):
    return getUser(userid)
@login_manager.unauthorized_handler
def unauthorized():
   return render_template("error404.html")

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash(message='You have logged out. Hope to see you soon!',
          category='success')
    return redirect(url_for('index'))

@app.route('/cart')
@login_required
def cart():
    return render_template('cart.html', user = current_user)
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html')
@app.errorhandler(500)
def page_not_found():
    return render_template('error404.html')
@app.errorhandler(401)
def page_not_found():
    return render_template('error404.html')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        basic_input()
        print("OK")

    app.run(debug=True)



