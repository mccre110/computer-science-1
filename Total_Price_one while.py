print ("Let's Calculate Total Price") 

#input price
price_float = float(input("Price? $"))
tax_float = float(input("Sales Tax? %"))

while price_float < 0 or tax_float <0:
    if price_float < 0:
        print (" (%s) : Price Invalid - Less Than Zero" %(price_float))
        price_float = float(input("Price? $"))
    else:
        print ("(%s) : Tax Invalid - Less Than Zero" %(tax_float))
        tax_float = float(input("Sales Tax? %"))

#calc and print if price and tax are good
tax_float/=100
total_float = price_float * (1 + tax_float)
print ("$ %s" %(total_float))

