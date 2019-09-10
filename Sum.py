#ask for how many times to loop and set pre-loop variables
loop_int = int(input("How many numbers would you like to add? :"))
number_int = 1
sum_int = 0

#initiate loop and set math for loop
while loop_int > 0:
    num_int = int(input(" Enter Number %s : " % (number_int)))
    number_int += 1
    sum_int += num_int
    loop_int -= 1

#print total
print (" Your total is : %s" %(sum_int))
    
