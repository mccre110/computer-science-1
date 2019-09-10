#import random for chance of dying randomly
import random

#preloop variable for loop control
next_room = 1

#fetch random death variable
random_death = random.randint(1,50)

#welcome line
print ("Hello there, You woke up in a strange room.")

#initiate loop with exit being next_room = 0
#conditionals for room control and selection
#next_room = 0 means win, next_room = 8 means death
while next_room != 0:

    #Starting Room
    if next_room == 1:
        print ("Would you like to go to the bathroom or door to the hall?")
        sel = input ("'b' or 'h' : ")
        if sel == "b":
            next_room = 2
        elif sel == "h":
            next_room = 3
        else:
            print(" Try again : ")

    #Bathroom - Dead end    
    elif next_room == 2:
        print ("This is the bathroom, sorry no windows")
        sel = input("Press 'b' to go back : ")
        if sel == "b":
            next_room = 1
        else:
            print(" Try again : ")
            
    #Hall            
    elif next_room == 3:
        print ("Welcome to the hall. Attic or Kitchen?")
        sel = input("'a' or 'k' : ")
        if sel == "a":
            next_room = 4
        elif sel == "k":
            next_room = 5
        else:
            print(" Try again : ")

    #Attic - Death
    elif next_room == 4:
        print ("You fell climbing the ladder.")
        next_room = 8

    #Kitchen
    elif next_room == 5:
        print ("You found the Kitchen. There's a window and a door to the garage : ")
        sel = input("'w' or 'g' : ")
        if sel == "w":
            #Chance of Death Conditional
            if random_death > 40:
                next_room=8
                random_death = random.randint(1,50)
            else:
                next_room = 6
        elif sel == "g":
            next_room = 7
        else:
            print(" Try again : ")

    #Window - Win
    elif next_room == 6:
        print ("You broke the glass and escaped with some scratches")
        next_room = 0

    #Gaarage - Death
    elif next_room == 7:
        print ("You tripped and fell into a black hole")
        next_room = 8

    #Death Conditional
    else:
        again = input("You Died - Try Again? y/n : ")
        if again == "y":
            next_room = 1

        else:
            print ("Game Over")
            break

#Win Conditional
else:
    print ("You Won - Bye")
