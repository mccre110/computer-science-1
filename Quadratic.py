import math #math.sqrt

#Prompt for a,b,c - Convert to float
a_float = float(input("a: "))
b_float = float(input("b: "))
c_float = float(input("c: "))

#Handles Complex Input
while ((b_float**2)-(4*a_float*c_float)) < 0:
    print ("Invalid input (Complex) Try Again : ")
    a_float = float(input("a: "))
    b_float = float(input("b: "))
    c_float = float(input("c: "))

#Actual math and print results
pos_quad = (-b_float+(math.sqrt((b_float**2)-(4*a_float*c_float))))/(2*a_float)
neg_quad = (-b_float-(math.sqrt((b_float**2)-(4*a_float*c_float))))/(2*a_float)
print (neg_quad,pos_quad)
