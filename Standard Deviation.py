#Variance and Standard Deviation
import math

#Preloop Variables
ulist = []
uinput = 1
num = 0

#Input Loop
while uinput>=0:
    uinput = int(input("Enter a Value : "))
    if uinput >=0:
        ulist.append (uinput)
ulist.sort()    

#Math and Sort Loop
avg = sum(ulist)/len(ulist)
for x in ulist:
    num += (x-avg)**2
dev = math.sqrt(num/len(ulist))

print ("Sorted List: ",ulist)
print ("Average: ",avg)
print ("Standard Deviation: ", dev)
