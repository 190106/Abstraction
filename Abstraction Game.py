from random import randint
start = 1


def mainMenu():
    while start == 1:
        choice = input("Enter '1' to go left, Enter '2' to go right, Enter 3 to exit the game\n")
        global random1
        global random2
        random1 = randint(1,2)
        random2 = randint(1,2)

        if choice == "1":
            left()

        elif choice == "2":
            right()

        elif choice == "3":
            stop()

        else:
            print ("invalid")


def left():
    if random1 == 1:
        print ("you were killed by the monster")
        stop()
    elif random1 == 2:
        choice2 = input("You venture on through the cave and reach another intersection. "
               "Enter '1' to go left again, Enter '2' to go right\n")
        if random2 == int(choice2):
            print ("you were killed by the monster")
            stop()
        else:
            print ("You reach the end of the cave and reach the treasure congratulations!\n")
            print (random2)
            stop()




def right():
    if random1 == 2:
        print ("you were killed by the monster")
        stop()
    elif random1 == 1:
        choice2 = input("You venture on through the cave and reach another intersection."
               "Enter '2' to go right again, Enter 1 to go left\n")
        if random2 == int(choice2):
            print ("you were killed by the monster")
            stop()
        else:
            print ("You reach the end of the cave and reach the treasure congratulations!\n")
            print (random2)
            stop()


def stop():
    global start
    start = 0

mainMenu()
