from service import *
def basic_input():
    f = '''Салат из капусты с кукурузой и ветчиной
    Салат домашний с майонезом
    Салат по-деревенски
    Салат Винегрет
    Салат из капусты с морковкой
    Салат по-деревенски 
    Суп картофельный с курицей
    Лапша куриная
    Крем-суп из тыквы
    Крем-суп овощной
    Рассольник с говядиной
    Борщ с курицей
    Компот из сухофруктов
    Напиток из шиповника
    Напиток ягодный
    Напиток каркаде
    Компот из яблок
    Напиток из шиповника
    '''.split("\n")


    for i in range(6):
        addAppetizer(name = f[i])

    for i in range(6, 12):
        addDish(name = f[i])
    for i in range(12, 18):
        addDrink(name = f[i])


    apps = db.session.query(Appetizer).all()
    dshs = db.session.query(Dish).all()
    drks = db.session.query(Drink).all()

    for i in range(6):
        lun = addLunch(apps[i].id, dshs[i].id, drks[i].id)

    user = addUser()
    addOrder(user.id, lun.id)



