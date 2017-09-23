class Item(object):
    def __init__(self, name, attack, armor, weight, price):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.weight = weight
        self.price = price


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def print_items(self):
        print('\t'.join(['Name', 'Atk', 'Arm', 'Lb', 'Val']))
        for item in self.items.values():
            print('\t'.join([str(x) for x in [item.name, item.attack, item.armor, item.weight, item.price]]))


inventory = Inventory()
inventory.add_item(Item('Sword', 5, 1, 15, 2))
inventory.add_item(Item('Armor', 0, 10, 25, 5))
inventory.print_items()


print("Welcome to Voltaire! the new fun text based adventure game")
print("The rules are simple  ")
Char = input("What is your name?")
print("Welcome", Char,"Let us begin your adventure!")

def beginning():
    start = input("you are in a large forest")
    if start.lower == "up":
        print("you try to go up but just end up falling back down")
        beginning()
    elif start.lower == "forward":
        print("you move forward")
    elif start.lower == "loot":
        print("You found some")
def forest1():
    f1 = input("You enter a dense forest with many trees around you")
def forest2():
    f2 = input()
def forest3():
    f3 = input()

def outsidehouse():
    out = input("The trees part. You come across a large white house with a lamp and a mail box outside")

def cave():
    c = input("you enter a large cave you can hear a running water and other noises further down but you may need to go further down to hear them more clearly")
def depths():
    d = input()
