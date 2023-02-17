from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *
from service import *
app = Flask(__name__)

@app.route('/')
def index():
   return "it works"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:eralex@localhost:5432/postgres_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()# <--- create db object.
        # dish1 = addDish() # псевдо добавление
        # print("Added Dish")
        # addDrink()
        # addAppetizer()
        db.session.commit()

    app.run(debug=True)

