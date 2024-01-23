# Class definition,getter,setter
class Human:
    #class attribute
    species = "Homo sapiens"

    def __init__(self, age):
        self.age = age

    def get_age(self):
        print("Retrieving age.")
        return self._age

    def set_age(self, age):
        print(f"Setting age to { age }")
        self._age = age


 # Instance Method Definition
class Dog:
  def bark(self):
    print("Woof!")

fido = Dog()
fido.bark()
# Woof!


class MyStore:

    def sign_in(self, user):
        self.user = user

    def current_user(self):
        return self.user

    def item(self, item):
        self.item = item

    def item_price(self, price):
        self.item_price = price

    def shopping_cart(self):
        self.shopping_cart = list()

    def add_item_to_cart(self, item):
        self.shopping_cart.append(item)


