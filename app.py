from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_migrate import Migrate
from models import *
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask import Flask,redirect, url_for, render_template, escape, abort, request, flash
from service import *
from basic_input import *
from datetime import date


DBUSER = 'postgres'
DBPASS = 'eralex'
DBHOST = 'localhost'
DBPORT = '5432'
DBNAME = 'project'

app = Flask(__name__)
app.secret_key = 'secret'

# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
#         user=DBUSER,
#         passwd=DBPASS,
#         host=DBHOST,
#         port=DBPORT,
#         db=DBNAME)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:eralex@localhost:5432/project_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = u'Please log in to access this page.'
login_manager.login_message_category = 'error'
migrate = Migrate(app, db)

local_cart=[]


@app.route('/',methods=['GET', 'POST'])
def index():
    day_of_week = datetime.now().weekday()
    lunches = []
    lunches.append(db.session.query(Lunch).filter_by(id = day_of_week*3 + 1).scalar())
    lunches.append(db.session.query(Lunch).filter_by(id = day_of_week*3 + 2).scalar())
    lunches.append(db.session.query(Lunch).filter_by(id = day_of_week*3 + 3).scalar())
    if (lunches is None or lunches == []):
        return render_template('eror404.html')
    addit = "/cart" if (logged_in()) else "/cart_empty"
    if request.method == 'POST':
        id = int(request.form['lunch_id'])
        qty = int(request.form['qty'])

        if not logged_in():
            flash(message="You aren't logged in!", category="warning")
            return redirect(url_for("index", lunches = lunches, activeT = "active", activeW = "", addition = addit))
        global local_cart


        matching = [d for d in local_cart if d['lunch_id'] == id]
        if matching:
            matching[0]['qty'] += qty
        else:
            local_cart.append(dict({'lunch_id': id, 'qty': qty, 'lunch' : db.session.query(Lunch).filter_by(id = id).scalar()}))
    if not logged_in():
        reg = ""
    else: reg = "/" + current_user.name
    return render_template("index.html",lunches = lunches,
                          activeT = "active", activeW = "", addition = addit, registered = reg)

@app.route('/week')
def weekPage():
    addit = "/cart" if (logged_in()) else "/cart_empty"
    if not logged_in():
        reg = ""
    else: reg = "/" + current_user.name
    return render_template("week.html", lunches = db.session.query(Lunch).all(),
                           activeT = "", activeW = "active", style_name = "week", addition = addit, registered = reg)

@app.route('/cart_empty')
def cart_empty():
    return render_template("cart_empty.html", lunches = db.session.query(Lunch).all(),
                           activeT = "active", activeW = "active", style_name = "week", addition = '/cart_empty',
                           registered = "")

@app.route('/account', methods=['GET', 'POST'])
def registerPage():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')

        if (name !=None and password!=None and login!=None ):
            user = addUser(login = login, password = password,name = name, status = True)
            login_user(user, remember=True)
            return redirect(url_for('accountPage', name = user.name), code = 301)
        elif (password!=None and login!=None):
            user = db.session.query(Users).filter_by(login = login, password = password).first()
            if user != None:
                login_user(user, remember=True)
                return redirect(url_for('accountPage', name = user.name),  code= 301)
        flash('Wrong login or password', 'danger')

    addit = "/cart" if (logged_in()) else "/cart_empty"
    if not logged_in():
        reg = ""
    else: reg = "/" + current_user.name
    return render_template("account.html", addition = addit, registered = reg)

@app.route('/account/<name>')
@login_required
def accountPage(name):
    name=escape(name)
    user = db.session.query(Users).filter_by(name =name).first()
    if (user is None):
        return render_template("error404.html")
    orders_of_day = [] if (user.status) else db.session.query(Orders).filter(func.DATE(Orders.date) == date.today()) # is employee
    lunches = [] if (user.status) else sorted(db.session.query(Lunch).all()[:18], key = lambda x: x.id)
    print(lunches)
    # transaction statistics:
    orders_all = [0]*18 # for lunches
    for i in range(18):
        #orders_all[i] = len(db.session.query(Orders).filter_by(id = i).all())
        orders_all[i] = random.randint(0, 100)
    print(orders_all)


    return render_template('userPage.html', user = user, addition= "/cart", registered = "/"+current_user.name,
                           orders = orders_of_day, lunches = lunches, orders_all = orders_all,
                           student = "invisible" if (current_user.status) else "")

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
    global local_cart
    local_cart = []
    flash(message='You have logged out. Hope to see you soon!',
          category='success')
    return redirect(url_for('index', addition="/cart_empty", registered = ""))

@app.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    global local_cart
    if request.method == 'POST':
        user = db.session.query(Users).filter_by(id = current_user.get_id()).first()
        print(user.name)
        for el in local_cart:
            addOrder(user.id, el['lunch'].id)
        local_cart = []

    return render_template('cart.html', user = current_user, cart = local_cart, addition = "/cart",
                           registered = "/"+current_user.name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html')
@app.errorhandler(500)
def page_not_found():
    return render_template('error404.html')
@app.errorhandler(401)
def page_not_found():
    return render_template('error404.html')

def logged_in(): return current_user.get_id() is not None
flag = True
if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        if (flag):
            flag = False
            basic_input()
        print("OK")

    app.run(debug=True)



