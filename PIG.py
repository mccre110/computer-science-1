import random

# game of pig
print("Let's Play Pig")

# preloop variables
scoreh = 0
scorec = 0

# Initiate Loop
while scorec < 100 and scoreh < 100:

    # Player Turn
    print(" You: %s | Computer: %s" % (scoreh, scorec))
    print("- - - - - - - - - -Human Playing- - - - - - - - - - ")
    rolltotal = 0
    roll = random.randint(1, 6)
    sel = str(0)
    print(" You rolled a %s" % (roll))
    while roll > 1 and sel != "h":
        sel = input("Roll again or Hold (r/h) : ")
        if sel == "r":
            rolltotal += roll
            roll = random.randint(1, 6)
            print(" You rolled : %s" % (roll))
        elif sel == "h":
            rolltotal += roll
            scoreh += rolltotal
        else:
            print("Try Again")

    # Computer Turn
    print("- - - - - - - - Computer Playing - - - - - - - - - - ")
    rolltotal = 0
    roll = random.randint(1, 6)
    while roll != 1 and rolltotal < 20:
        rolltotal += roll
        roll = random.randint(1, 6)
    scorec += rolltotal

# End Clause
print("Good Game")
if scoreh > scorec:
    print("You Won!")
else:
    print("You Lost")
print(" You: %s | Computer: %s" % (scoreh, scorec))
