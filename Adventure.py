#Owen Matyi 9/24/17

#Lists
Keys = {"HouseKey": False, "GateKey": False, "LockboxKey": False, "DrownedChestKey": False, "RedGem": False, "BlueGem":False, "GreenGem":False, "PurpleGem":False, "AnctientIdol": False }

#starting variables
life = 100


def changegold(amount):
    global gold
    gold += amount
    print("You gained", amount, "Gold. You now have", gold)


def changelife(hpchange):
    global life
    life += hpchange
    if life <= 0:
        dead()
    print("You lost", hpchange, "Life. you have", life, "life left.")


def dead():
    print("you are dead try again next time!")
    exit(0)


def start():
    print("Welcome to Voltaire! the new fun text based adventure game")
    print("The rules are simple  ")


def charactercreation():
    char = input("What is your name?")
    print("Welcome", char, "Let us begin your adventure!")
    beginning()


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
