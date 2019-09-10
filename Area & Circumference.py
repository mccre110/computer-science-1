#Calculate Area and Circumfernce of a Circle

import math

radius_str = input ("Radius?")
radius_int = int(radius_str)

cir = 2 * math.pi * radius_int
area = math.pi * radius_int**2

print ("Circumference:  %s Area:  %s" % (cir,area))
