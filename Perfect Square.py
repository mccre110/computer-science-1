import math
number_int = int(input("Enter a Number : "))
Test = False


while Test == False:
    sq_int = math.sqrt(number_int)
    if number_int % sq_int == 0:
         print ("%s : Perfect Square!" %(number_int))
         Test = True
    else:
        number_int = int(input("(Not a perfect square. Try Again : "))
        
