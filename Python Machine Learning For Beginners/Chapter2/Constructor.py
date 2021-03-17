# Script 18

class Fruit:

    name = "apple";
    price = 10;

    def __init__(self, fruit_name, fruit_price):

        Fruit.name = fruit_name;
        Fruit.price = fruit_price;

    def eat_fruit(self):
        print("Fruit has been eaten.");

f = Fruit("Orange", 15);
f.eat_fruit();
print(f.name);
print(f.price);