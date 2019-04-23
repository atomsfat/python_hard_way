from sys import exit


def gold_room():
    print("There is a room full of good. How much do yout take")
    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        print("Learn to type a number")

    if how_much < 50:
        print("You are not too greedy")
        exit(0)
    else:
        dead("You are dead bastard")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another room.")
    print("How are going to move the bear?")
    bear_moved = False
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear look at you then slap your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now")
            bear_moved = True
        elif choice == "open door" and bear_moved:
            gold_room()


def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it, whatever states at you and you go insane")
    print("Do you flee for you life or eat your head")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room")
    print("There is a room to your right and left")
    print("Which one do you take")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room util you starve")


start()
