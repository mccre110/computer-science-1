#xsimple guessing game

import random

num = random.randint (0,100)

guess = int(input("Enter a Number 0-100 : "))

while 0 <= guess <= 100:
    if guess > num:
        print ("You guessed too high")
        guess = int(input("Enter a Number 0-100 : "))
    elif guess < num:
        print ("You guessed too low")
        guess = int(input("Enter a Number 0-100 : "))
    else:
        print ("You guessed it : " , num)
        break

else:
    print ("Quiter :" , num)
