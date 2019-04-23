print("You enter a dark room with two doors. Do you go through door #1 or door #2")
door = input(" >")

if door == "1":
    print("there is a giant bear here eating a cheese cake")
    print("What do you want to do ?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")
    if bear == "1":
        print("The bear eat your face off. Good job!.")
    elif bear == "2":
        print("The bear eat your legs off. Good job!.")
    else:
        print(f"well, doing {bear} is probable better")
elif door == "2":
    print("You stare into the endless abyss a Voldemort retina")
    print("1. Blueberries")
    print("2. Yellow jackets clothespins")
    print("3. Understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind o jello")
        print("Good job")
    else:
        print("The insanity root your eyes into a pool of muck")
        print("Good job")
else:
    print("You stumble around and fall on knife and die. Good job!.")
