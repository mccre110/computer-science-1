
#set pre-loop variables and ask for input
loop_int = int(input("What number would you like the consecutive total of? : "))
num_int = 1
sum_int = 0

#establish loop sums consec until loop int gets substracted to 1
while loop_int > 0:
    sum_int += num_int
    num_int += 1
    loop_int -= 1

#print output
print ("Your total is : %s" % (sum_int))
