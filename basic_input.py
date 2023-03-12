import random

from service import *
def basic_input():
    f = '''
Olivier salad
Korean carrots
Cabbage salad with cucumber
Caesar salad
Crab salad
Greek salad
Borsch
Pickle with chicken
Soup with vermicelli
Cabbage soup with sauerkraut
Pea soup
Vegetable puree soup
Vegetable puree soup
Cabbage soup with sauerkraut
Mashed potatoes
Pea soup
Soup with vermicelli
Pea soup
Cabbage rolls
Pasta bolognese
Pilaf with beef
Mashed potatoes
Quinoa with beef
Pasta in cream sauce
Apple juice
Cherry juice
Orange juice
Compote
Apple juice
Cherry juice
    '''.split("\n")
    apps =[]
    dshs =[]
    drks =[]
    f = f[1:]
    for i in range(18):
        apps.append(addAppetizer(name = f[i%6], photo= f[i%6].lower().replace(" ", "_")))

    for i in range(6, 6+18):
        dshs.append(addDish(name = f[i], photo=f[i].lower().replace(" ", "_")))

    drinks = ["drink_1", "drink_3"]

    for i in range(6+18, 12+18):
        drks.append(addDrink(name = f[i], photo = drinks[i%2]))

    for i in range(6 + 18, 12 + 18):
        drks.append(addDrink(name=f[i], photo=drinks[i%2]))
    for i in range(6 + 18, 12 + 18):
        drks.append(addDrink(name=f[i], photo=drinks[i%2]))

    types = ["bsns", "veg", "std"]
    day_of_week =["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for i in range(18):
        lun = addLunch(name = types[i%3] + " "+day_of_week[i//3],appetizer_id=apps[i].id,
                       dish_id=dshs[i].id,drink_id= drks[i].id,
                       likes_amount= random.randint(1, 100), dislikes_amount=random.randint(1,100))

    user = addUser(status = False)

# from app import app
# with app.app_context():
#     basic_input()



