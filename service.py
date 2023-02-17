from models import *

def addAppetizer(name = "Appetizer_1", photo = "img.img"):
    appetizer = Appetizer(name = name, photo = photo)
    db.session.add(appetizer)
    return appetizer

def addDish(name = "Appetizer_1", photo = "img.img"):
    dish = Dish(name = name, photo = photo)
    db.session.add(dish)
    return dish

def addDrink(name = "Appetizer_1", photo = "img.img"):
    drink = Drink(name = name, photo = photo)
    db.session.add(drink)
    return drink
def addLunch(appetizer_id:Appetizer, dish_id: Dish, drink_id:Drink, likes_amount = 0, dislikes_amount =0):
    lunch = Lunch(appetizer_id = appetizer_id, dish_id = dish_id, drink_id = drink_id,
                  likes_amount =likes_amount, dislikes_amount = dislikes_amount)
    db.session.add(lunch)
    return lunch



