import random
roll = 0
rolltotal = 0

while True:
    roll = random.randint(1,6)
    while rolltotal < 20:
        rolltotal += roll
        roll = random.randint(1,6)
        print (rolltotal)
    
    
