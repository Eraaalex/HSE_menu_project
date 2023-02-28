from models import *

def addUser(login ="admin@admin.ru", password = "qwerty1",name = "Admin", status = True):
    user = Users(id = None, login = login, password = password, name = name, status = status)

    db.session.add(user)
    db.session.commit()
    return user

def addAppetizer(name = "Appetizer_1", photo = "img.img"):
    appetizer = Appetizer(name = name, photo = photo)
    db.session.add(appetizer)
    db.session.commit()
    return appetizer

def addDish(name = "Appetizer_1", photo = "img.img"):
    dish = Dish(name = name, photo = photo)
    db.session.add(dish)
    db.session.commit()
    return dish

def addDrink(name = "Appetizer_1", photo = "img.img"):
    drink = Drink(name = name, photo = photo)
    db.session.add(drink)
    db.session.commit()
    return drink
def addLunch(appetizer_id:Appetizer, dish_id: Dish, drink_id:Drink, likes_amount = 0, dislikes_amount =0):
    lunch = Lunch(appetizer_id = appetizer_id, dish_id = dish_id, drink_id = drink_id,
                  likes_amount =likes_amount, dislikes_amount = dislikes_amount)
    db.session.add(lunch)
    db.session.commit()
    return lunch
# def addAccount(login ="admin@yandex.ru", password = "qwerty1", name = "eraaalex", status = True):
#     acc = Account(login = login, password = password, name = name, status = status)
#     db.session.add(acc)
#     db.session.commit()
#     return acc
# def addFeedback(user_id:Users, text):
#     feedback = Feedback(user_id = user_id,text = text)
#     db.session.add(feedback)
#     db.session.commit()
#     return feedback


