import random

from service import *
def basic_input():
    f = '''
Оливье
Морковь по-корейски
Салат из капусты с огурцом
Цезарь
Салат крабовый
Греческий салат
Борщ
Рассольник с курицей
Суп с вермишелью
Щи с квашеной капустой
Суп гороховый
Суп пюре овощной
Суп пюре овощной
Щи с квашеной капустой
пюре
Суп гороховый
Суп с вермишелью
Суп гороховый
Ленивые голубцы
Паста болоньезе
Плов с говядиной
Пюре
Киноа с говядиной
Макароны в сливочном соусе
Яблочный сок
Вишневый сок
Апельсиновый сок
Компот
Яблочный сок
Вишневый сок
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



